from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from ..models import Producto, Pedido, LineaPedido
from ..forms import ProductoForm, PedidoForm

# PROTEGER VISTAS CON LOGIN
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def index(request):
    return render(request, "index.html")

@login_required
def productos(request):
    productos = Producto.objects.all() #No usamos el all por que devuelve objetos de la classe
    # render es como view en laravel, es para que cargue el html, 
    # pasamos request para poder usar variables de usuario
    return render(request, "productos.html", {"productos": productos})

# usamos las funciones por defecto de validar formularios
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Producto, id=product_id)
    peso_kg = int(request.POST.get('peso_kg', 1))

    # busca un Pedido con esos valores, si no existe, lo crea"
    # created True si acaba de crearlo, False si ya existía
    cart, created = Pedido.objects.get_or_create(
        usuario_web=request.user,
        estado='carrito'
    )

    linea, created = LineaPedido.objects.get_or_create(
        pedido=cart,
        producto=product,
        defaults={'precio_unidad': product.precio_unidad, 'peso_kg': peso_kg}
    )
    if not created:
        linea.peso_kg += peso_kg
        linea.save()

    return redirect('cart')

@login_required
def cart(request):
    try:
        cart = Pedido.objects.get(usuario_web=request.user, estado='carrito')
        lineas = cart.lineas.all()
        total = sum(linea.precio_unidad for linea in lineas)
    except Pedido.DoesNotExist:
        cart = None
        lineas = []
        total = 0
    return render(request, 'resumen_carrito.html', {'cart': cart, 'lineas': lineas, 'total': total})

@login_required
def checkout(request):
    try:
        cart = Pedido.objects.get(usuario_web=request.user, estado='carrito')
    except Pedido.DoesNotExist:
        return redirect('cart')

    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=cart)
        if form.is_valid():
            # crea el objeto pedido pero no lo guarda en la bdd, por el commit = False
            pedido = form.save(commit=False) 
            pedido.estado = 'confirmado'
            pedido.save() # ahora si se guarda en la bdd, directamente sobre el objeto
            return redirect('pedido_confirmado')
    else:
        form = PedidoForm(instance=cart)

    lineas = cart.lineas.all()
    total = sum(linea.caja * linea.precio_unidad for linea in lineas)
    return render(request, 'checkout.html', {'form': form, 'lineas': lineas, 'total': total})

@login_required
def pedido_confirmado(request):
    # Assuming the last confirmed pedido
    try:
        pedido = Pedido.objects.filter(usuario_web=request.user, estado='confirmado').latest('fecha_creacion')
    except Pedido.DoesNotExist:
        return redirect('cart')
    return render(request, 'pedido_confirmado.html', {'pedido': pedido})



# EXTRA PARA SACAR TODOS LOS PRODUCTOS, NO SE USA
def producto_list_api(request):
    productos = list(Producto.objects.values()) # esto devuelve lista de diccionarios
    return JsonResponse(productos, safe=False)

    

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'agrivall/producto_form.html'
    success_url = reverse_lazy('producto_list') # calcula la ruta /agrivall/productos, solo el string, 
                                                # se usa lazy para que la genere cuando la use. 

# Hace esto por defecto, si no hay post, redirige a la vista del final, si hay post y el form es válido,
# lo inserta en Product, por que el ProductForm es del model Product, y que sea válido significa que tenga
# los campos que se definen en el ProductForm

# if request.method == "POST":
#     form = ProductoForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect("producto_list")
# else:
#     form = ProductoForm()

# return render(request, "agrivall/producto_form.html", {"form": form})

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'agrivall/producto_form.html'
    success_url = reverse_lazy('producto_list')


# si hay método post, se valida el formulario y se actualiza el producto.
# si el método es get, se carga el formulario del html con los datos del producto existente

# def producto_update(request, pk): # saca la pk de la url
# producto = Producto.objects.get(pk=pk)

# if request.method == "POST":
#     form = ProductoForm(request.POST, instance=producto)
#     if form.is_valid():
#         form.save()
#         return redirect("producto_list")
# else:
#     form = ProductoForm(instance=producto) # Esto permite crear el formulario del producto directamente

# return render(request, "agrivall/producto_form.html", {"form": form})


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'agrivall/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')

# def producto_delete(request, pk):
# producto = Producto.objects.get(pk=pk)

# if request.method == "POST":
#     producto.delete()
#     return redirect("producto_list")

# return render(
#     request,
#     "agrivall/producto_confirm_delete.html",
#     {"object": producto}
# )



from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from ..models import Producto, Pedido, LineaPedido
import pdb


# CREAR LINEA PEDIDO DEL FORMULARIO
@login_required
def crear_linea_pedido(request):
    """
    Crea una linea de pedido (pedido en el carro) a partir del formulario de productos.
    Si se viene con get, se manda al índice
    """
    if request.method != "POST":
        return redirect("index")

    producto_id = request.POST.get("producto_id")
    producto = get_object_or_404(Producto, id=producto_id)

    pedido, creado = Pedido.objects.get_or_create(
        usuario_web=request.user,
        estado="carrito"
    )

    LineaPedido.objects.create(
        pedido=pedido,
        producto=producto,
        precio_unidad=producto.precio_unidad,
        peso_kg=producto.peso_kg
    )

    # sacamos el contador de productos que tiene el usuario en el carrito
    # para ello, usamos el pedido, ya que tiene asociado el id de usuario
    pedido = Pedido.objects.filter(
        usuario_web=request.user,
        estado='carrito'
    ).first()

    # si hay pedido en el carrito, contamos los productos
    if not pedido:
        return JsonResponse({"cart_count": 0})

    cart_count = pedido.lineas.count()

    return JsonResponse({
        'ok': True,
        "cart_count": cart_count
    })


def eliminar_linea_pedido(request):
    """
    función para eliminar un pedido del carrito de la compra
    """
    if request.method == "POST":
        linea_pedido_id = request.POST.get('linea_pedido_id')
        linea_pedido = get_object_or_404(LineaPedido, id=linea_pedido_id)
        pedido = linea_pedido.pedido
        linea_pedido.delete()

        # si se ha borrado el último producto del carrito, se borra el pedido
        # ya que si no crecen exponencialmente
        if not pedido.lineas.exists():
            pedido.delete()

        return redirect('cart')


# RESUMEN CARRITO ANTES DE COMPRAR
def resumen_carrito(request):
    pedido = Pedido.objects.filter(
        usuario_web=request.user,
        estado="carrito"
    ).first()

    lineas = []
    total = 0

    if pedido:
        lineas = pedido.lineas.select_related("producto").all()

        for linea in lineas:
            total += linea.precio_unidad * linea.caja

    return render(request, "resumen_carrito.html", {
        "pedido": pedido,
        "lineas": lineas,
        "total": total,
    })
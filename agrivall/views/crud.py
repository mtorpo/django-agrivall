


from django.shortcuts import render, get_object_or_404, redirect, render
from django.http import Http404
from agrivall.models import Producto, Pedido
from agrivall.forms import ProductoForm, PedidoForm


from django.contrib.auth.decorators import user_passes_test

def es_superuser(user):
    return user.is_authenticated and user.is_superuser


# ===========================
# GESTIÓN DE VISTAS
# ===========================
@user_passes_test(es_superuser)
def dashboard(request):

    return render(request, 'crud/dashboard.html')

# panel productos
@user_passes_test(es_superuser)
def panel_productos(request):

    productos = Producto.objects.all()

    return render(request, 'crud/panel_productos.html', {"productos": productos})


# panel pedidos
@user_passes_test(es_superuser)
def panel_pedidos(request):

    # pedidos = Pedido.objects.all().filter()
    # pedidos = Pedido.objects.filter(estado="confirmado") # solo los que ya haya confimado el cliente
    pedidos = Pedido.objects.exclude(estado="carrito") # todos los que no sean carrito

    return render(request, 'crud/panel_pedidos.html', {"pedidos": pedidos})

# ===========================
# CRUD PARA PRODUCTOS
# ===========================

@user_passes_test(es_superuser)
def crear_producto(request):

    form = ProductoForm(request.POST)

    if form.is_valid() and request.method == "POST":
        producto = form.save()
    
    else:
        return render(request, "crud/ver_producto.html")

    return redirect('dashboard')

@user_passes_test(es_superuser)
def ver_producto(request):

    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")
    
    producto_id = request.POST.get("producto_id")

    producto = Producto.objects.get(id=producto_id)

    if producto:
        return render(request, "crud/ver_producto.html", {"producto": producto, "producto_id": producto_id})
    
@user_passes_test(es_superuser)
def editar_producto(request):

    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")

    id_producto = int(request.POST.get("producto_id"))
    producto = get_object_or_404(Producto, id=id_producto)

    form = ProductoForm(
        request.POST,
        request.FILES,
        instance=producto
    )

    if form.is_valid():
        producto = form.save(commit=False)

        if request.POST.get("borrar_imagen"):
            producto.imagen.delete(save=False) # borra la imagen de /media/, pero no inserta en la bdd
            producto.imagen = None # borramos la referencia (esto lo hace automático, pero se deja por facilidad visual)

        producto.save()

    return redirect('panel_productos')

@user_passes_test(es_superuser)
def eliminar_producto(request):
    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")

    producto_id = request.POST.get("producto_id")

    producto = get_object_or_404(Producto, id=producto_id)

    producto.delete()

    return redirect("panel_productos")

    

# ===========================
# CRUD PARA PEDIDOS
# ===========================

@user_passes_test(es_superuser)
def editar_estado_pedido(request):

    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")

    pedido_id = int(request.POST.get("pedido_id"))
    nuevo_estado = request.POST.get("nuevo_estado")
    
    pedido = get_object_or_404(Pedido, id=pedido_id)

    if pedido.estado != nuevo_estado:
        pedido.estado = nuevo_estado
        pedido.save()
    
    return redirect('panel_pedidos')
        


    
    
    




from django.shortcuts import render, get_object_or_404, redirect, render
from django.http import Http404
from agrivall.models import Producto, Pedido, PostBlog, TipoPost
from agrivall.forms import ProductoForm, PedidoForm, PostBlogForm


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

    return redirect('panel_productos')

@user_passes_test(es_superuser)
def ver_producto(request):

    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")
    
    producto_id = request.POST.get("producto_id")

    producto = get_object_or_404(Producto, id=producto_id)

    if producto:
        return render(request, "crud/ver_producto.html", {"producto": producto})


def gestion_imagenes(request, instancia, imagen_anterior):
    # Se valida si han subido imagen
    hay_imagen_nueva = bool(request.FILES.get("imagen"))
    # Se valida si han pulsado borrar imagen
    borrar_imagen = bool(request.POST.get("borrar_imagen"))

    # Si han subido imagen, prevalece esta, y el botón de borrar no hace nada, pues subir una imagen ya implica borrar la anterior 
    if hay_imagen_nueva:
        instancia.save()
        # Se borra la anterior
        if imagen_anterior:
            instancia.imagen.storage.delete(imagen_anterior)

    # Si no se sube imagen y se pulsa borrar, se borra
    elif borrar_imagen:
        instancia.imagen = None
        instancia.save()

        if imagen_anterior:
            instancia.imagen.storage.delete(imagen_anterior)

    else:
        instancia.save()



@user_passes_test(es_superuser)
def editar_producto(request):

    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")

    producto = get_object_or_404(
        Producto,
        id=request.POST.get("producto_id")
    )

    imagen_anterior = producto.imagen.name if producto.imagen else None

    form = ProductoForm(
        request.POST,
        request.FILES,
        instance=producto
    )

    if form.is_valid():
        producto = form.save(commit=False)

        gestion_imagenes(request, producto, imagen_anterior)

    return redirect("panel_productos")

@user_passes_test(es_superuser)
def eliminar_producto(request):
    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")

    producto_id = request.POST.get("producto_id")

    producto = get_object_or_404(Producto, id=producto_id)

    # borramos imagen de producto si este se borra
    if producto.imagen:
        producto.imagen.delete(save=False)

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
        

# ========
# CRUD PARA BLOGS
# ========
@user_passes_test(es_superuser)
def panel_posts(request):

    posts = PostBlog.objects.all()

    return render(request, 'crud/panel_posts.html', {"posts": posts})

@user_passes_test(es_superuser)
def ver_post(request):

    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")
    
    post_id = request.POST.get("post_id")

    post = get_object_or_404(PostBlog, id=post_id)

    tipos = TipoPost.objects.all()

    if post:
        return render(request, "crud/ver_post.html", {"post": post, "tipos": tipos})
    
    
@user_passes_test(es_superuser)
def eliminar_post(request):
    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")

    post_id = request.POST.get("post_id")

    post = get_object_or_404(PostBlog, id=post_id)

    # borramos imagen de producto si este se borra
    if post.imagen:
        post.imagen.delete(save=False)

    post.delete()

    return redirect("panel_posts")


@user_passes_test(es_superuser)
def editar_post(request):

    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")

    post = get_object_or_404(
        PostBlog,
        id=request.POST.get("post_id")
    )

    imagen_anterior = post.imagen.name if post.imagen else None

    form = PostBlogForm(
        request.POST,
        request.FILES,
        instance=post
    )

    if form.is_valid():
        post = form.save(commit=False)

        gestion_imagenes(request, post, imagen_anterior)
    else:
        print(form)

    return redirect("panel_posts")


@user_passes_test(es_superuser)
def crear_post(request):

    form = PostBlogForm(request.POST)

    if form.is_valid() and request.method == "POST":
        post = form.save()

    else:
        tipos = TipoPost.objects.all()
        return render(request, "crud/ver_post.html", {"tipos": tipos})

    return redirect('panel_posts')
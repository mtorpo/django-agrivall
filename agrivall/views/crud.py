


from django.shortcuts import render, get_object_or_404, redirect, render
from django.http import Http404
from agrivall.models import Producto
from agrivall.forms import ProductoForm


from django.contrib.auth.decorators import user_passes_test

def es_superuser(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(es_superuser)
def dashboard(request):

    productos = Producto.objects.all()

    return render(request, 'crud/dashboard.html', {"productos": productos})

    


# CRUD PARA PRODUCTOS
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
            producto.imagen.delete(save=False)
            producto.imagen = None

        producto.save()

    return redirect('dashboard')

@user_passes_test(es_superuser)
def eliminar_producto(request):
    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")

    producto_id = request.POST.get("producto_id")

    producto = get_object_or_404(Producto, id=producto_id)

    producto.delete()

    return redirect("dashboard")

    


        


        


    
    
    

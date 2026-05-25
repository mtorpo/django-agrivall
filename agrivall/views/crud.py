


from django.shortcuts import render, get_object_or_404, redirect, render
from django.http import Http404
from agrivall.models import Producto
from agrivall.forms import ProductoForm


def dashboard(request):

    productos = Producto.objects.all()

    return render(request, 'crud/dashboard.html', {"productos": productos})

    


# CRUD PARA PRODUCTOS
def crear_producto(request):

    
    mensaje = "Error al crear producto"

    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")

    form = ProductoForm(request.POST)

    producto = None

    if form.is_valid():

        producto = form.save()

        mensaje = "Producto creado correctamente"

    return "hola"


def ver_producto(request):

    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")
    
    producto_id = request.POST.get("producto_id")

    producto = Producto.objects.get(id=producto_id)

    form = ProductoForm(instance=producto)

    if producto:
        return render(request, "crud/ver_producto.html", {"producto": form, "producto_id": producto_id})
    

def editar_producto(request):

    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")

    id_producto = int(request.POST.get("producto_id"))
    producto = get_object_or_404(Producto, id = id_producto)

    form = ProductoForm(request.POST, instance=producto)

    if form.is_valid():
        form.save()

    return redirect('dashboard')


def eliminar_producto(request):
    if request.method != "POST":
        raise Http404("Ups! Parece que te has perdido")

    producto_id = request.POST.get("producto_id")

    producto = get_object_or_404(Producto, id=producto_id)

    producto.delete()

    return redirect("dashboard")

    


        


        


    
    
    

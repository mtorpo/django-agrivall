from django import forms
from .models import Producto, Pedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'stock', 'descripcion', 'precio_unidad']


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'direccion', 'cp']
        # campo total a mano


        # Esto nos permite que cuando django genere los campos de manera automática
        # con el form.as_p, que use estas configuraciones, tipo texto y con la clase indicada
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class':'form-control rounded-pill',
                'placeholder':'Nombre'
            }),

            'direccion': forms.TextInput(attrs={
                'class':'form-control rounded-pill',
                'placeholder':'Dirección'
            }),

            'cp': forms.TextInput(attrs={
                'class':'form-control rounded-pill',
                'placeholder':'Código postal'
            })
        }
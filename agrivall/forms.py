from django import forms
from .models import Producto, Pedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'stock', 'descripcion', 'precio_unidad', 'imagen', 'peso_kg']


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



from django.contrib.auth.forms import AuthenticationForm
from django import forms


# CREAMOS UN FORM PARA LOGIN, y no usamos el propio, para aplicar boostrap sobre los form.campos
# por que con el por defecto, form.campo ya crea un input lo que sea, no podemos poner la class
# Aprovechamos y definimos los textos para los errores
class LoginForm(AuthenticationForm):
    
    error_messages = {
        "invalid_login": (
            "Usuario o contraseña incorrectos."
        )
    }

    # Bootstrap
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded-pill",
                "placeholder": "Usuario"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control rounded-pill",
                "placeholder": "Contraseña"
            }
        )
    )


# Con el register solo para el bootstrap
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control rounded-pill",
                "placeholder":"Usuario"
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control rounded-pill",
                "placeholder":"Contraseña"
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control rounded-pill",
                "placeholder":"Repetir contraseña"
            }
        )
    )

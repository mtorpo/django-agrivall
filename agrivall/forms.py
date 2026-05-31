from django import forms
from .models import Producto, Pedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio_unidad', 'imagen', 'peso_kg', 'variedad', 'disponible']


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'direccion', 'cp', 'telefono', 'metodo_pago', 'email']
        # campo total a mano

    # Esto es para indicar, que sean los campos REQUIRED SOLO en el form. Con django la forma habitual es no hacer blank ni null en el 
    # model, eso lo hace automáticamente required por defecto. Pero como en la BDD sí pueden ser null, pero queremos que al crear el form
    # NO, entonces aquí interceptamos el form una vez creado el modelo, y le cambiamos solo ese campo. La otra alternativa es redefinir aquí
    # todas las variables y ponerle el required, pero hay que duplicar el entramado de Charfield, max min... etc. Y digo duplicar por que sí o sí
    # en ese caso tendríamos que tener también el modelo existiendo.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        self.fields['direccion'].required = True
        self.fields['cp'].required = True
        self.fields['telefono'].required = True
        self.fields['metodo_pago'].required = True
        self.fields['email'].required = True



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


# Con el register solo para el bootstrap
# from django.contrib.auth.forms import UserCreationForm
# from django import forms


# class RegisterForm(UserCreationForm):

import factory
from django.contrib.auth.models import User
from .models import Producto, Pedido, LineaPedido
import random
from django.contrib.auth.hashers import make_password

# Al heredar de DjangoModelFactory podemos usar el create y craete_batch  
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    # no soporta unique, tan solo podemos hacerlo así para que sea único
    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@mail.com")

    # usamos Lazy function para que cada vez que se llame a la clase, el random sample se ejecute, si no
    # se ejecuta una sola vez al cargar la clase, y aun que se llame, los valores son los mismos.
    password = factory.LazyAttribute(lambda obj: make_password(obj.username))
    
    # email = factory.Faker("email")



class ProductoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Producto
        #exclude = ("variedades_list",) # Se pueden excluir variables para que la factory no lo interprete 
        #como un campo del modelo

    nombre = factory.Sequence(lambda n: f"Producto {n}")
    stock = factory.Faker("random_int", min=1, max=100)
    descripcion = factory.Faker("sentence")
    precio_unidad = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
    imagen = factory.django.ImageField(color="blue")
    peso_kg = factory.Faker("random_int", min=1, max=5)



class PedidoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pedido

    usuario_web = factory.SubFactory(UserFactory)
    estado = "carrito"

    nombre = factory.Faker("name")
    direccion = factory.Faker("street_address")
    cp = factory.Faker("postcode")
    total = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
    telefono = factory.Faker("phone_number")
    metodo_pago = "bizum"


class LineaPedidoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LineaPedido

    pedido = factory.SubFactory(PedidoFactory)
    producto = factory.SubFactory(ProductoFactory)

    # usamos el precio del producto para mantener coherencia
    precio_unidad = factory.LazyAttribute(
        lambda obj: obj.producto.precio_unidad
    )

    peso_kg = factory.Faker("random_int", min=1, max=3)

from django.contrib.auth.models import User
from agrivall.models import Producto, Pedido, LineaPedido
from django.core.management.base import BaseCommand
from agrivall.factories import UserFactory, ProductoFactory, PedidoFactory, LineaPedidoFactory


class Command(BaseCommand):
    help = "Vacía y rellena de nuevo la base de datos con datos de ejemplo"

    def handle(self, *args, **kwargs):
        LineaPedido.objects.all().delete()
        Pedido.objects.all().delete()
        Producto.objects.all().delete()
        User.objects.filter(is_superuser=False).delete() # no nos cargamos el super user

        usuarios = UserFactory.create_batch(2)
        productos = ProductoFactory.create_batch(10)

        for usuario in usuarios:
            for i in range(1):
                pedido = PedidoFactory.create(
                    usuario_web=usuario
                )

                # añadimos líneas al pedido
                LineaPedidoFactory.create(
                    pedido=pedido,
                    producto=productos[i % len(productos)]
                )

        self.stdout.write(self.style.SUCCESS("Base de datos rellenada correctamente"))
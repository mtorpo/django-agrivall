from django.db import models
from django.contrib.auth.models import User


# TIPOS
# models.CharField(max_length=255)
# models.IntegerField()
# models.DecimalField(max_digits=10, decimal_places=2)
# models.ImageField(upload_to="productos/", blank=True, null=True)
# models.JSONField()

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="productos/", blank=True, null=True)
    variedad = models.JSONField()

    class Meta:
        db_table = "productos"

    def __str__(self):
        return self.nombre

# pedido final, con datos de dirección...
class Pedido(models.Model):
    ESTADOS = [
        ("carrito", "Carrito"),
        ("confirmado", "Confirmado"),
        ("enviado", "Enviado"),
        ("entregado", "Entregado"),
    ]

    usuario_web = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pedidos")
    estado = models.CharField(max_length=20, choices=ESTADOS, default="carrito")

    nombre = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    cp = models.CharField(max_length=20, blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        db_table = "pedidos"

    def __str__(self):
        return f"Pedido {self.id} - {self.estado}"

# pedidos para el carrito, tan solo info de lo que se pide
class LineaPedido(models.Model):
    #el FK crea una relación uno a muchos, desde cada Pedido a sus lineaPedido. El related name
    # define como vamos a acceder a esta relación. También se crea a la inversa, acceder a un Pedido
    # desde una lineapedido
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="lineas")
    #el related name nos permite acceder a un uno a muchos, desde cada Pedido a sus lineaPedido.
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="lineas_pedido")

    variedad = models.CharField(max_length=100)
    caja = models.IntegerField(default=1)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    peso = models.IntegerField()
    
    class Meta:
        db_table = "lineas_pedido"

    def __str__(self):
        return f"{self.producto.nombre} x {self.caja}"
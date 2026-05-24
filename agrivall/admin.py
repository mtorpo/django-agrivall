from django.contrib import admin
from agrivall.models import Pedido, SemanaCasilla, Producto, LineaPedido, Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Producto._meta.fields]
    list_filter = ("nombre",)
    search_fields = ("nombre","descripcion")

admin.site.register(LineaPedido)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pedido._meta.fields]
    list_filter = ("estado",)
    search_fields = ("nombre",)

@admin.register(SemanaCasilla)
class SemanaCasillaAdmin(admin.ModelAdmin):
    # list_display = ("ano", "numero_sem", "estado", "precio", "descriptor")
    list_display = [field.name for field in SemanaCasilla._meta.fields]
    list_filter = ("ano", "estado")
    search_fields = ("descriptor",)
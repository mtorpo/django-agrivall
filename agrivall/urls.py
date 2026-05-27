from django.urls import path
from .views.views import *
from .views.blog import *
from .views.casilla import *
from .views.crud import dashboard, ver_producto, editar_producto, eliminar_producto, crear_producto, panel_productos, panel_pedidos, editar_estado_pedido

urlpatterns = [
    # MAIN
    path('', index, name='index'),
    # path('agrivall/', index, name='index'),

    # PRODUCTOS
    # VIsta
    path('productos/', productos, name='productos'),    
    # Main function, gestión de todo
    path('checkout/', checkout, name='checkout'),
    path('pedido_confirmado/', pedido_confirmado, name='pedido_confirmado'),
    
    # AUTO CRUD
    # path('productos/crear/', ProductoCreateView.as_view(), name='producto_create'),
    # path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'),
    # path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_delete'),
    
    path("crear-linea-pedido/", crear_linea_pedido, name="crear_linea_pedido"),
    path("eliminar-linea-pedido/", eliminar_linea_pedido, name="eliminar-linea-pedido"),

    # CASILLA
    path('casilla/', casilla, name='casilla'),

    # BLOG
    path('blog/', blog, name='blog'),

    # CRUD
    path('dashboard/', dashboard, name='dashboard'),

    # CRUD - productos
    path('panel_productos/', panel_productos, name="panel_productos"),
    path('ver_producto/', ver_producto, name="ver_producto"),
    path('editar_producto/', editar_producto, name="editar_producto"),
    path('eliminar_producto/', eliminar_producto, name="eliminar_producto"),
    path('crear_producto/', crear_producto, name="crear_producto"),

    # CRUD - pedidos
    path('panel_pedidos/', panel_pedidos, name="panel_pedidos"),
    path('editar_estado_pedido/', editar_estado_pedido, name="editar_estado_pedido")
]

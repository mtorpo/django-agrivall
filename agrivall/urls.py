from django.urls import path
from .views.views import *
from .views.blog import *
from .views.casilla import *

urlpatterns = [
    path('', index, name='index'),

    path('productos/', productos, name='productos'),
    
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),
    path('pedido_confirmado/', pedido_confirmado, name='pedido_confirmado'),
    
    path('productos/crear/', ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_delete'),
    
    path("crear-linea-pedido/", crear_linea_pedido, name="crear_linea_pedido"),
    path("eliminar-linea-pedido/", eliminar_linea_pedido, name="eliminar-linea-pedido"),

    path('casilla', casilla, name='casilla'),

    path('blog', blog, name='blog')
]
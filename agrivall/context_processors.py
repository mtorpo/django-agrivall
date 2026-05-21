from .models import Pedido

def carrito(request):
    if request.user.is_authenticated:
        pedido = Pedido.objects.filter(
            usuario_web=request.user,
            estado="carrito"
        ).first()

        if pedido:
            total_lineas = pedido.lineas.count()
        else:
            total_lineas = 0
    else:
        total_lineas = 0

    return {
        "carrito_total": total_lineas
    }
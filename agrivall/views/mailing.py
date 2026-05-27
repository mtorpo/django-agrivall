from django.core.mail import send_mail
from django.conf import settings


def mail_functionality(new_subject = "Pedido registrado", new_message = ""):

    send_mail(
        subject=new_subject,
        message=new_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False
                )
    

# =================================
# MAILING PERSONALIZADO PARA PEDIDO
# =================================
def montar_mensaje_pedido(pedido):

    return f"""
Nuevo pedido confirmado

ID pedido: #{pedido.id}
Cliente: {pedido.nombre}
Código postal: {pedido.cp}
Total: {pedido.total} €
Fecha: {pedido.fecha_creacion}

Revisa el pedido completo desde el panel de administración.
"""

def enviar_mail_pedido(pedido):

    mensaje = montar_mensaje_pedido(pedido)

    send_mail(
        subject=f"Nuevo pedido confirmado #{pedido.id}",
        message=mensaje,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=False
    )
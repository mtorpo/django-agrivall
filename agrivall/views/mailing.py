from django.core.mail import send_mail
from django.conf import settings

# para resolver la url a dashboard fuera de django
from django.urls import reverse

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
def enviar_mail_pedido(request, pedido):

    dashboard_url = request.build_absolute_uri(
    reverse("dashboard")
    )

    mensaje =  f"""
Nuevo pedido confirmado

ID pedido: #{pedido.id}
Cliente: {pedido.nombre}
Código postal: {pedido.cp}
Total: {pedido.total} €
Fecha: {pedido.fecha_creacion}

Revisa el pedido completo desde el panel de administración:
{dashboard_url}
"""
    tema = f"Nuevo pedido confirmado #{pedido.id}"
    
    mail_functionality(tema, mensaje)
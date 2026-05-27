from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.urls import reverse


def enviar_mail_pedido(request, pedido):

    panel_pedidos_url = request.build_absolute_uri(
        reverse("panel_pedidos")
    )

    asunto = f"Nuevo pedido confirmado #{pedido.id}"

    # Texto plano (fallback)
    mensaje_texto = f"""
Nuevo pedido confirmado

ID pedido: #{pedido.id}
Cliente: {pedido.nombre}
Código postal: {pedido.cp}
Total: {pedido.total} €
Fecha: {pedido.fecha_creacion}

Panel:
{panel_pedidos_url}
"""

    # HTML con botón
    mensaje_html = f"""
    <html>
        <body style="font-family: Arial, sans-serif;">
            
            <h2>Nuevo pedido confirmado</h2>

            <p><strong>ID pedido:</strong> #{pedido.id}</p>
            <p><strong>Cliente:</strong> {pedido.nombre}</p>
            <p><strong>Código postal:</strong> {pedido.cp}</p>
            <p><strong>Total:</strong> {pedido.total} €</p>
            <p><strong>Fecha:</strong> {pedido.fecha_creacion}</p>

            <br>

            <a href="{panel_pedidos_url}"
               style="
                    background-color:#000;
                    color:#fff;
                    padding:12px 20px;
                    text-decoration:none;
                    border-radius:6px;
                    display:inline-block;
                    font-weight:bold;
               ">
                Ver pedido en el dashboard
            </a>

        </body>
    </html>
    """

    email = EmailMultiAlternatives(
        subject=asunto,
        body=mensaje_texto,
        from_email=settings.EMAIL_HOST_USER,
        to=[settings.EMAIL_HOST_USER]
    )

    email.attach_alternative(mensaje_html, "text/html")
    email.send()
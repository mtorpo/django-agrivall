from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.urls import reverse


def notify_admin_mail(request, pedido):

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
    # clase para poder incrustar el html y que el servidor de correo interprete. Manda versión texto y html,
    # el servidor elige
    email = EmailMultiAlternatives(
        subject=asunto,
        body=mensaje_texto,
        from_email=settings.EMAIL_HOST_USER,
        to=[settings.EMAIL_HOST_USER]
    )

    email.attach_alternative(mensaje_html, "text/html")
    email.send()


from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.urls import reverse



def notify_client_mail(pedido):

    asunto = f"AGRIVALL - Pedido confirmado #{pedido.codigo_seguimiento}"

    # ==========================
    # Resumen de productos HTML
    # ==========================
    lineas_html = ""

    # Obtenemos productos a través de pedido
    for linea in pedido.lineas.all():
        lineas_html += f"""
        <tr>
            <td>{linea.producto.nombre}</td>
            <td>{linea.peso_kg} kg</td>
            <td>{linea.precio_unidad} €</td>
        </tr>
        """

    # ==========================
    # Texto plano (fallback)
    # ==========================
    mensaje_texto = f"""
Pedido confirmado

Hola {pedido.nombre},

Hemos recibido correctamente tu pedido.

Código de seguimiento: {pedido.codigo_seguimiento}

Total: {pedido.total} €

Gracias por confiar en Agrivall.
"""

    # ==========================
    # HTML
    # ==========================
    mensaje_html = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333;">

        <h2>Pedido confirmado</h2>

        <p>Hola {pedido.nombre},</p>

        <p>
            Hemos recibido correctamente tu pedido.
            Gracias por confiar en Agrivall.
        </p>

        <p>
            <strong>Código de seguimiento:</strong>
            {pedido.codigo_seguimiento}
        </p>

        <p>
            <strong>Fecha:</strong>
            {pedido.fecha_creacion}
        </p>

        <h3>Resumen del pedido</h3>

        <table
            cellpadding="8"
            cellspacing="0"
            border="1"
            style="
                border-collapse: collapse;
                width: 100%;
                margin-bottom: 20px;
            "
        >
            <thead>
                <tr style="background-color: #f5f5f5;">
                    <th>Producto</th>
                    <th>Peso</th>
                    <th>Precio</th>
                </tr>
            </thead>

            <tbody>
                {lineas_html}
            </tbody>
        </table>

        <p>
            <strong>Total:</strong>
            {pedido.total} €
        </p>

        <h3>Dirección de entrega</h3>

        <p>
            {pedido.direccion}<br>
            {pedido.cp}
        </p>

        <br>

        <p>
            Te avisaremos cuando el pedido entre en preparación.
        </p>

        <p>
            Gracias por confiar en Agrivall.
        </p>

    </body>
    </html>
    """

    email = EmailMultiAlternatives(
        subject=asunto,
        body=mensaje_texto,
        from_email=settings.EMAIL_HOST_USER,
        to=[pedido.email]
    )

    email.attach_alternative(mensaje_html, "text/html")
    email.send()
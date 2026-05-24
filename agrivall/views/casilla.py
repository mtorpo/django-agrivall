from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from agrivall.models import SemanaCasilla

# validación de email
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def casilla(request):
    """
    Función para cargar casilla y gestionar la paginación de las semanas
    """
    semanas = SemanaCasilla.objects.all().order_by("numero_sem")

    paginator = Paginator(semanas, 4)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # en caso de que se reserve, se valida mail y se actualiza estado semana
    if request.method == "POST":
        semana_id = int(request.POST.get("semana_id"))
        Semana = get_object_or_404(SemanaCasilla, id=semana_id)
        print(Semana)
        # validamos email, por que cualquiera puede solicitar una semana
        try:
            user_email = request.POST.get("email")
            validate_email(user_email)
            print("Email válido")
        except ValidationError:
            print("Email inválido")

        Semana.estado = "pre-reserva"
        Semana.save()

    return render(request, "casilla.html", {
        "page_obj": page_obj
    })


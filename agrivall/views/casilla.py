from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from agrivall.models import SemanaCasilla

# validación de email
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from agrivall.forms import ReservaCasillaForm

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

        form = ReservaCasillaForm(request.POST)

        if form.is_valid():
            # Si es válido, actualizamos la semana en la bdd y redirijimos a la página sin form y sin datos
            semana_id = int(request.POST.get("semana_id"))
            Semana = get_object_or_404(SemanaCasilla, id=semana_id)            

            Semana.estado = "pre-reserva"
            Semana.save()

            return redirect("casilla")

    else:
        # si no es válido, 
        form = ReservaCasillaForm()
    
    # En caso de no POST o POST con form inválido, volvemos a la web con el form que había (o vacío si no era POST)
    return render(request, "casilla.html", {
        "page_obj": page_obj,
        "form": form,
    })


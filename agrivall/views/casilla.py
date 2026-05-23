from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
import json

from agrivall.models import DiaReserva


def casilla(request):
    dias = DiaReserva.objects.all().order_by("fecha")

    dias_reserva = [
        {
            "fecha": dia.fecha.isoformat(),
            "reservado": dia.reservado,
        }
        for dia in dias
    ]

    return render(request, "casilla.html", {
        "dias_reserva_json": json.dumps(dias_reserva, cls=DjangoJSONEncoder)
    })
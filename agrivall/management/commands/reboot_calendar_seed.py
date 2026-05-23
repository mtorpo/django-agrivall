from datetime import date, timedelta
from django.core.management.base import BaseCommand
from agrivall.models import DiaReserva


class Command(BaseCommand):
    help = "Vacía y rellena la base de datos"


    def crear_dias_reserva(self):

        # Borra todas las fechas
        DiaReserva.objects.all().delete()

        self.stdout.write("Borrando fechas anteriores...")

        año = 2026

        fecha_inicio = date(año, 1, 1)
        fecha_fin = date(año, 12, 31)

        fecha_actual = fecha_inicio

        while fecha_actual <= fecha_fin:

            DiaReserva.objects.create(
                fecha=fecha_actual
            )

            fecha_actual += timedelta(days=1)

        self.stdout.write(
            self.style.SUCCESS(
                "Fechas creadas correctamente"
            )
        )


    def handle(self, *args, **kwargs):

        self.crear_dias_reserva()
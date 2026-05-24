from datetime import date, timedelta
from django.core.management.base import BaseCommand
from agrivall.models import SemanaCasilla


class Command(BaseCommand):
    help = "Vacía y rellena semanas de reserva"


    def crear_semanas_reserva(self):

        SemanaCasilla.objects.all().delete()

        self.stdout.write(
            "Borrando semanas anteriores..."
        )

        año = 2026

        fecha_actual = date(año, 1, 1)

        semanas_creadas = set()


        while fecha_actual.year <= año:

            # ISO devuelve:
            # (año_iso, numero_semana, dia_semana)
            año_iso, numero_sem, _ = fecha_actual.isocalendar()

            # Evita duplicar semanas
            if (año_iso, numero_sem) not in semanas_creadas:

                semanas_creadas.add(
                    (año_iso, numero_sem)
                )

                fecha_inicio = fecha_actual - timedelta(
                    days=fecha_actual.weekday()
                )

                fecha_fin = fecha_inicio + timedelta(days=6)

                SemanaCasilla.objects.create(

                    ano=año_iso,

                    numero_sem=numero_sem,

                    estado="libre",

                    precio=450,

                    descriptor=(
                        f"{fecha_inicio.strftime('%d/%m/%Y')} - "
                        f"{fecha_fin.strftime('%d/%m/%Y')}"
                    )
                )

            fecha_actual += timedelta(days=1)

        self.stdout.write(
            self.style.SUCCESS(
                "Semanas creadas correctamente"
            )
        )


    def handle(self, *args, **kwargs):

        self.crear_semanas_reserva()
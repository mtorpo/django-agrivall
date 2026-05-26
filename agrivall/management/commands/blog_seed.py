from django.core.management.base import BaseCommand
from agrivall.models import TipoPost, PostBlog


class Command(BaseCommand):
    help = "Crea posts iniciales del blog"

    def handle(self, *args, **kwargs):
        tipo_cultivos, _ = TipoPost.objects.get_or_create(tipo="cultivos")
        tipo_ecologia, _ = TipoPost.objects.get_or_create(tipo="ecología")
        tipo_cursos, _ = TipoPost.objects.get_or_create(tipo="cursos")

        PostBlog.objects.get_or_create(
            titulo="Cómo mejorar la producción de cerezas en primavera",
            defaults={
                "noticia": "La primavera es una etapa clave para el desarrollo del cerezo.",
                "tipo": tipo_cultivos,
            },
        )

        PostBlog.objects.get_or_create(
            titulo="Agricultura ecológica: pequeños cambios con gran impacto",
            defaults={
                "noticia": "La agricultura ecológica busca reducir químicos y fomentar procesos naturales.",
                "tipo": tipo_ecologia,
            },
        )

        PostBlog.objects.get_or_create(
            titulo="Nuevo curso: iniciación al cultivo sostenible",
            defaults={
                "noticia": "Abrimos una nueva formación sobre técnicas modernas de cultivo sostenible.",
                "tipo": tipo_cursos,
            },
        )

        self.stdout.write(self.style.SUCCESS("Posts de blog creados correctamente"))
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class MainPagesSitemap(Sitemap):

    # Google ya no usa esto, lo detecta el solo
    # priority = 0.8
    # changefreq = "weekly"

    # Esto son los names de las urls principales de mi web. Esto le da a Google contexto
    # Esto genera un listado de urls en xml con mis urls construidas
    # <url>
    #     <loc>https://daw-agrivall.es/</loc>
    # </url>
    def items(self):
        return [
            "index",
            "productos",
            "casilla",
            "blog",
        ]

    # este reverse es el que saca la url real a partir del nombre
    def location(self, item):
        return reverse(item)
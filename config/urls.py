"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# settings → para acceder a MEDIA_URL y MEDIA_ROOT.
# static → función que crea las rutas para servir archivos.
from django.conf import settings
from django.conf.urls.static import static
# Nuestro login manual para aplicar boostrap en el form.campo
from agrivall.forms import LoginForm

# LOGIN
from django.urls import path
from django.contrib.auth import views as auth_views
from agrivall.views.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("agrivall.urls")),
    # 
    path("login/", auth_views.LoginView.as_view(template_name="auth/login.html",
        authentication_form=LoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Hace que cuando alguien acceda a una URL como: /media/productos/camiseta.jpg
# Django vaya a buscar el archivo en: MEDIA_ROOT/productos/camiseta.jpg


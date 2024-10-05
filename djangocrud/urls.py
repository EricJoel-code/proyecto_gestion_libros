"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from libreria import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.inicio, name='inicio'),
    path("registro/", views.registro, name='registro'),
    path("libreria/", views.libreria, name='libreria'),
    path("agregar/libro/", views.agregar_libro, name='agregar_libro'),
    path("libreria/<int:libro_id>/", views.detalle_libro, name='detalle_libro'),
    path("libreria/<int:libro_id>/eliminar", views.eliminar_libro, name='eliminar_libro'),
    path("salir/", views.salir, name='salir'),
    path("iniciar_sesion/", views.inicio_sesion, name='iniciar_sesion'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

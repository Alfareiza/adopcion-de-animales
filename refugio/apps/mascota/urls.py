from django.contrib import admin
from django.urls import path

# Aqui deben ir todas las urls de la aplicación
from refugio.apps.mascota import views

urlpatterns = [
    path('', views.index_mascota, name='index'),
    path('nuevo/', views.mascota_view, name='mascota_crear')
]

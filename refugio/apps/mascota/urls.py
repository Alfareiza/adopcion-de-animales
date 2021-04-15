from django.contrib import admin
from django.urls import path

# Aqui deben ir todas las urls de la aplicación
from refugio.apps.mascota import views

app_name = 'mascota'
urlpatterns = [
    path('', views.index_mascota, name='index'),
    path('nuevo/', views.mascota_create, name='mascota_crear'),
    path('listar/', views.mascota_list, name='mascota_listar'),
    path('editar/<int:id_mascota>/', views.mascota_edit, name='mascota_editar')
]

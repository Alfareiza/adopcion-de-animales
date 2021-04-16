from django.contrib import admin
from django.urls import path

# Aqui deben ir todas las urls de la aplicación
from refugio.apps.mascota import views

app_name = 'mascota'
urlpatterns = [
    path('', views.index_mascota, name='index'),
    path('nuevo/', views.MascotaCreate.as_view(), name='mascota_crear'),
    path('listar/', views.MascotaList.as_view(), name='mascota_listar'),
    path('editar/<int:pk>/', views.MascotaUpdate.as_view(), name='mascota_editar'),
    path('eliminar/<int:pk>/', views.MascotaDelete.as_view(), name='mascota_eliminar')
]

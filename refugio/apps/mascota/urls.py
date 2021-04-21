from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

# Aqui deben ir todas las urls de la aplicación
from refugio.apps.mascota import views

app_name = 'mascota'
urlpatterns = [
    path('', views.index_mascota, name='index'),
    path('nuevo/', login_required(views.MascotaCreate.as_view()), name='mascota_crear'),
    path('listar/', login_required(views.MascotaList.as_view()), name='mascota_listar'),
    path('editar/<int:pk>/', login_required(views.MascotaUpdate.as_view()), name='mascota_editar'),
    path('eliminar/<int:pk>/', login_required(views.MascotaDelete.as_view()), name='mascota_eliminar'),
    path('listado/', views.listadodemascotas, name='listado')
]

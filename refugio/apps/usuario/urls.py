from django.contrib import admin
from django.urls import path

# Aqui deben ir todas las urls de la aplicación
from refugio.apps.usuario import views

app_name = 'usuario'
urlpatterns = [
    # path('', views.index_adopcion, name='index'),
    path('registrar/', views.RegistroUsuario.as_view(), name='registrar'),
]

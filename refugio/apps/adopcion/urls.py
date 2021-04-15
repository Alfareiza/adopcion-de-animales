from django.contrib import admin
from django.urls import path

# Aqui deben ir todas las urls de la aplicación
from refugio.apps.adopcion import views

app_name = 'adopcion'
urlpatterns = [
    path('', views.index_adopcion, name='home')
]

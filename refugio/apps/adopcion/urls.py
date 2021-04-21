from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

# Aqui deben ir todas las urls de la aplicación
from refugio.apps.adopcion import views

app_name = 'adopcion'
urlpatterns = [
    path('', views.index_adopcion, name='home'),
    path('solicitud/listar/',  login_required(views.SolicitudList.as_view()(), name='solicitud_listar'),
    path('solicitud/nuevo/',  login_required(views.SolicitudCreate.as_view()(), name='solicitud_crear'),
    path('solicitud/editar/<int:pk>/',  login_required(views.SolicitudUpdate.as_view()(), name='solicitud_editar'),
    path('solicitud/eliminar/<int:pk>/',  login_required(views.SolicitudDelete.as_view()(), name='solicitud_eliminar')
]

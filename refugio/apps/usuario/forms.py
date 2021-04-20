from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from refugio.apps.adopcion.models import Persona, Solicitud


class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username': "Nombre de usuario", 'first_name': "Nombres", 'last_name': "Apellidos", 'e-mail': "E-mail"}
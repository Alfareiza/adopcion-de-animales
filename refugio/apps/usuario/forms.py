from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from refugio.apps.adopcion.models import Persona, Solicitud


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        labels = {'username': "Nombre de usuario", 'first_name': "Nombres", 'last_name': "Apellidos",
                  'email': "E-mail"}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'password': forms.PasswordInput(attrs={'class': 'form-control'})}

from django import forms

from refugio.apps.adopcion.models import Persona, Solicitud


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'telefono',
                  'edad', 'correo', 'direccion']
        labels = {'nombres': 'Nombres',
                  'apellidos': 'Apellidos',
                  'telefono': 'Telefono',
                  'edad': 'Edad',
                  'correo': 'Correo',
                  'direccion': 'Dirección'}
        widgets = {'nombres': forms.TextInput(attrs={'class': 'form-control'}),
                   'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
                   'telefono': forms.TextInput(attrs={'class': 'form-control'}),
                   'edad': forms.NumberInput(attrs={'class': 'form-control'}),
                   'correo': forms.EmailInput(attrs={'class': 'form-control'}),
                   'direccion': forms.TextInput(attrs={'class': 'form-control'}),
                   }


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['numero_mascotas', 'razones']
        labels = {'numero_mascotas': 'Número de Mascotas',
                  'razones': 'Razones para adoptar'}
        widgets = {'numero_mascotas': forms.TextInput(attrs={'class': 'form-control'}),
                   'razones': forms.Textarea(attrs={'class': 'form-control'})
                   }

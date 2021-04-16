from django import forms

from refugio.apps.mascota.models import Mascota


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'sexo', 'edad_aproximada',
                  'fecha_de_rescate', 'raza', 'comentarios', 'persona',
                  'vacuna']
        labels = {'nombre': 'Nombre',
                  'sexo': 'Sexo',
                  'edad_aproximada': 'Edad Aproximada',
                  'fecha_de_rescate': 'Fecha de Rescate',
                  'raza': 'Raza',
                  'comentarios': 'Comentarios',
                  'persona': 'Adoptante',
                  'vacuna': 'Vacuna'
                  }
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                   'sexo': forms.TextInput(attrs={'class': 'form-control'}),
                   'edad_aproximada': forms.TextInput(attrs={'class': 'form-control'}),
                   'fecha_de_rescate': forms.TextInput(attrs={'class': 'form-control'}),
                   'raza': forms.TextInput(attrs={'class': 'form-control'}),
                   'comentarios': forms.TextInput(attrs={'class': 'form-control'}),
                   'persona': forms.Select(attrs={'class': 'custom-select'}),
                   'vacuna': forms.CheckboxSelectMultiple(),
                   }

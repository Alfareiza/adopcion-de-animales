from django.contrib import admin

# Los modelos son registrados aqui para que puedan ser manipulados en el admin de django
from refugio.apps.adopcion.models import Persona

admin.site.register(Persona)
from django.contrib import admin

# Los modelos son registrados aqui para que puedan ser manipulados en el admin de django
from refugio.apps.mascota.models import Vacuna, Mascota

admin.site.register(Mascota)
admin.site.register(Vacuna)
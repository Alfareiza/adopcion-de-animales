from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from refugio.apps.usuario.forms import RegistroForm


class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('mascota:mascota_listar')

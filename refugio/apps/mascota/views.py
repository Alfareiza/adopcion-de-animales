from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from refugio.apps.mascota.forms import MascotaForm


def index_mascota(request):
    return render(request, 'mascota/mascota.html')


def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:index')  # Va a la app mascota y busca la url que tenga name=index
    else:
        form = MascotaForm()

    return render(request, 'mascota/mascota_form.html', {'form': form})

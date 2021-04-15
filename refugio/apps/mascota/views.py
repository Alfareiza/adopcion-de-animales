from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from refugio.apps.mascota.forms import MascotaForm
from refugio.apps.mascota.models import Mascota


def index_mascota(request):
    return render(request, 'mascota/mascota.html')


def mascota_create(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mascota:index'))
        else:
            return render(request, 'mascota/mascota_form.html', {'form': form}, status=400)

    form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', context={'form': form})


def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    return render(request, 'mascota/mascota_list.html', context={'mascotas': mascota})


def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('mascota:mascota_listar'))
    return render(request, 'mascota/mascota_form.html', context={'form': form})

from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from refugio.apps.mascota.forms import MascotaForm
from refugio.apps.mascota.models import Mascota


def index_mascota(request):
    return render(request, 'mascota/mascota.html')


def mascota_create(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mascota:mascota_listar'))
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


def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return HttpResponseRedirect(reverse('mascota:mascota_listar'))
    return render(request, 'mascota/mascota_delete.html', context={'mascota': mascota})


# Intro https://docs.djangoproject.com/en/3.2/topics/class-based-views/
# Detailed https://docs.djangoproject.com/en/3.2/ref/class-based-views/

# Cuando la vista es llamada, se va hacia template_name.
class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'


class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')


class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')


class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota:mascota_listar')


def listadodemascotas(request):
    lista = serializers.serialize('json', Mascota.objects.all())
    return HttpResponse(lista, content_type='application/json')

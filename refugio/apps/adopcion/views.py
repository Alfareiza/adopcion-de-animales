from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_adopcion(request):
    return HttpResponse('Pagina Principal del Site')
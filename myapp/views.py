from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. contiene la logica para manejar solicitudes http y manejar respuesta, interaccion del controlador

def home(request):
    return HttpResponse("Hola mmundo")
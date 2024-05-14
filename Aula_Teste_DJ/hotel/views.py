from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def homepage(request):
    # return HttpResponse("<h1> Hello World </h1>")
    context = {}
    dados_hotel = hotel.objects.all()
    context["dados_hotel"] = dados_hotel    
    return render(request,'homepage.html' , context)

def quartos(request):
    context = {}
    context2 = {}
    dados_quarto = quarto.objects.all() 
    dados_hotel = hotel.objects.all()
    
    context["dados_quarto"] = dados_quarto
    
    return render(request, 'quartos.html', context)
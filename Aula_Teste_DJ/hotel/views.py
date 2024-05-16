from django.shortcuts import render, HttpResponse
from .models import *
from .forms import FormNome

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

def nome (request):
    if request.method == "POST":
        form = FormNome(request.POST)
        if form.is_valid():
             
             var_nome = form.cleaned_data['nome']
             var_sobrenome = form.cleaned_data['sobrenome']
             var_email = form.cleaned_data['email']
             var_idade = form.cleaned_data['idade']
             var_endereco = form.cleaned_data['endereco']
             var_quarto = form.cleaned_data['quarto']
             var_data = form.cleaned_data['data']

             user = usuario(nome = var_nome, sobrenome = var_sobrenome, email = var_email, idade = var_idade, endereco = var_endereco, quarto = var_quarto, data = var_data)
             user.save()

             print(var_nome)
             print(var_sobrenome)
             print(var_email)
             print(var_idade)
             print(var_endereco)
             print(var_quarto)
             print(var_data)
             
             return HttpResponse("<h1 style=\"font-family: 'Courier New', Courier, monospace; background-color: #f5c2dac6; text-align: center; padding: 20px; padding-top: 50px; padding-bottom: 50px\">Reserva realizada com sucesso!<br> Em breve entraremos em contato com você para mais detalhes.<br>Obrigada por escolher o Hotel Senai!</h1>")
        
    else:
        form = FormNome()

    return render(request, "nome.html", {"form": form})
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('quartos', views.quartos, name='quartos'),
    path('nome', views.nome, name='nome'),
    path('cadastro', views.cadastro, name='cadastro'), 
    path('login', views.login, name='login')
]
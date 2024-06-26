from django.db import models
import datetime

# Create your models here.

TIPOS_QUARTOS = (
    ("SOLTEIRO", "Solteiro"),
    ("CASAL", "Casal"),
    ("CONFORTO","Conforto"),
    ("LUXO","Luxo")
)

class hotel(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    logo = models.ImageField(upload_to="logo/")

    def __str__(self):
        return self.titulo

class quarto(models.Model):
    tipo = models.CharField(max_length=15, choices=TIPOS_QUARTOS)
    disponibilidade = models.IntegerField()
    valor = models.FloatField(max_length=4)
    descricao = models.TextField(max_length=255)
    foto_quarto = models.ImageField(upload_to="Foto_Quarto/")
    # data_reserva = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.tipo

class usuario(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    idade = models.CharField(max_length=3)
    endereco = models.CharField(max_length=50)
    quarto = models.CharField(max_length=4)
    data = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


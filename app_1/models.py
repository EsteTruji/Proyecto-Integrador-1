from django.db import models

# Create your models here.

class Usuarios(models.Model):
    codigo = models.CharField(max_length=6)
    nombre = models.CharField(max_length=45)
    cantidadRecogida = models.IntegerField(default=0)

class Canecas(models.Model):
    caneca_id = models.CharField(max_length=6)
    sector = models.CharField(max_length=20)
    cantidadRecogida = models.IntegerField(default=0)
    tipo = models.CharField(max_length=10)

class Incentivos(models.Model):
	codigo = models.CharField(max_length=6)
	puntos = models.IntegerField(default=0)
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

#python manage.py makemigrations
#python manage.py sqlmigrate app_1 0001
#python manage.py migrate

#python manage.py shell
#from app_1.models import Usuarios
#usr5 = Usuarios(codigo = 'AAA000', nombre = 'Esteban Trujillo', cantidadRecogida = 25)
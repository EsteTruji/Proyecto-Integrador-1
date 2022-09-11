from tkinter import CASCADE
from django.db import models

# Create your models here.

class Usuario(models.Model):
	id_usuario = models.AutoField(primary_key=True, blank=False)
	nombre = models.CharField(max_length=45, null=False)

class Etiqueta(models.Model):
	id_archivo = models.CharField(primary_key=True, max_length=100, blank=False)
	Usuario_id_usuario = models.ForeignKey(Usuario, null= False, blank=False, on_delete=models.CASCADE)
	etiqueta = models.JSONField(null=False, blank=False)
	caneca = models.CharField(max_length=45, null=False, blank=False, choices=(('Ordinario','Ordinario'), ('Papel_Carton','Papel_Carton'), ('Plastico','Plastico'), ('Vidrio','Vidrio'), ('Organicos','Organicos'), ('Residuos_Peligrosos','Residuos_Peligrosos'), ('Aluminio','Aluminio')))
	fecha_etiquetado = models.DateTimeField(auto_now_add=True)

class Residuo(models.Model):
	Etiqueta_id_archivo = models.ForeignKey(Etiqueta, null=True, blank=False, on_delete=models.CASCADE)
	id_residuo = models.PositiveIntegerField(blank=False)
	
class Puntos(models.Model):
	Usuario_id_usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
	cantidad_puntos = models.PositiveIntegerField(default=0)
	fecha_puntos = models.DateTimeField(auto_now_add=True)

class Actividad(models.Model):
	Usuario_id_usuario = models.ForeignKey(Usuario, null= False, blank=False, on_delete=models.CASCADE)
	tipo_actividad = models.CharField(max_length=45, null=False, blank=False, choices=(('etiquetado','etiquetado'),('clasificado','clasificado')))
	fecha_actividad = models.DateTimeField(auto_now_add=True)

#python manage.py makemigrations
#python manage.py sqlmigrate app_1 0001
#python manage.py migrate

#python manage.py shell
#from app_1.models import Usuarios
#usr5 = Usuarios(codigo = 'AAA000', nombre = 'Esteban Trujillo', cantidadRecogida = 25)
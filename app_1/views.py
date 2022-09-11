from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import Puntos, Usuario

id2 = 1

def home(request):
    usuarios_obj = Usuario.objects.get(id_usuario = id2)
    return render(request, 'home.html', {'nombre':usuarios_obj.nombre})

def mis_incentivos(request):
    usuarios_obj = Usuario.objects.get(id_usuario = id2)
    puntos = Puntos.objects.get(Usuario_id_usuario = id2)
    return render(request, 'mis_incentivos.html', {'nombre':usuarios_obj.nombre, 'codigo':usuarios_obj.id_usuario, 'puntos':puntos.cantidad_puntos, 'fecha':puntos.fecha_puntos})

def mi_actividad(request):
    usuarios_obj = Usuario.objects.get(id_usuario = id2)
    puntos = Puntos.objects.get(Usuario_id_usuario = id2)
    return render(request, 'mi_actividad.html', {'nombre':usuarios_obj.nombre, 'codigo': usuarios_obj.id_usuario,'puntos': puntos.cantidad_puntos})

def filtrar_por(request):
    return render(request, 'filtrar_por.html')

def etiquetado(request):
    return render(request, 'etiquetado.html')

def etiquetaExito(request):
    material = request.POST['material']
    return render(request, 'exito_Etiquetado.html')
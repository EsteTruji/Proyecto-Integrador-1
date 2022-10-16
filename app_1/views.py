from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import *
import json
import os

id2 = 1

def home(request):
    usuarios_obj = Usuario.objects.get(id_usuario = id2)
    return render(request, 'home.html', {'nombre':usuarios_obj.nombre})

def mis_incentivos(request):
    usuarios_obj = Usuario.objects.get(id_usuario = id2)
    puntos_todos = Puntos.objects.filter(Usuario_id_usuario_id = id2)
    return render(request, 'mis_incentivos.html', {'puntos_todos': puntos_todos,'nombre':usuarios_obj.nombre})

def mi_actividad(request):
    usuarios_obj = Usuario.objects.get(id_usuario = id2)
    actividades = Actividad.objects.filter(Usuario_id_usuario_id = id2)
    return render(request, 'mi_actividad.html', {'actividades': actividades,'nombre':usuarios_obj.nombre})

def filtrar_por(request):
    return render(request, 'filtrar_por.html')

def etiquetado(request):
    return render(request, 'etiquetado.html')

def realizar_etiquetado(request):
    return render(request, 'realizar_etiquetado.html')    

def etiquetaExito(request):
    usuarios_obj = Usuario.objects.get(id_usuario = id2)
    material = request.POST['material']
    package_color = request.POST['package_color']
    bottle_cap = request.POST['bottle_cap']
    dirtiness = request.POST['dirtiness']
    packaging_type = request.POST['packaging-type']
    brand = request.POST['brand']
    reference = request.POST['reference']
    capacity = request.POST['capacity']
    damage = request.POST['damage']
    id_archivo1 = request.POST['id_archivo']


    pruebaEtiquetas = {
        'Material': material,
        'Package color': package_color,
        'Bottle cap': bottle_cap,
        'Dirtiness': dirtiness,
        'Packaging type': packaging_type,
        'Brand': brand,
        'Reference': reference,
        'Capacity (ml)': capacity,
        'Damage': damage
    }

    nombre_archivo = id_archivo1.split() 
    id_archivo1 = nombre_archivo[0];   

    nombre_carpeta = "Observaciones"
    ruta = os.path.abspath(nombre_carpeta)

    with open (os.path.join(ruta, id_archivo1+'.json'), 'w') as f:
        json.dump(pruebaEtiquetas, f)

    '''with open(os.path.join(dir, 'Etiqueta.json'), 'r') as f:
        pruebaEtiquetas = json.load(f)'''
        
        
    db_etiqueta = Etiqueta(id_archivo = id_archivo1, Usuario_id_usuario_id = usuarios_obj.id_usuario, Material = material, Package_color = package_color, Bottle_cap = bottle_cap, Dirtiness= dirtiness, Packaging_type = packaging_type, Brand = brand, Reference = reference, Capacity = capacity, Damage = damage)
    db_etiqueta.save()
    db_actividad = Actividad(Usuario_id_usuario_id = usuarios_obj.id_usuario, tipo_actividad = 'etiquetado')
    db_actividad.save()
    db_puntos = Puntos(cantidad_puntos = 5, Usuario_id_usuario_id = usuarios_obj.id_usuario)
    db_puntos.save()
    nombre_archivo = []
    return render(request, 'exito_Etiquetado.html')
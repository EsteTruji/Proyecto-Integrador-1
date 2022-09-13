from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import *
import json

id2 = 3

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

    with open ('prueba.json', 'w') as f:
        json.dump(pruebaEtiquetas, f)

    with open('prueba.json','r') as f:
        pruebaEtiquetas = json.load(f)
        jsonString = json.dumps(pruebaEtiquetas)
    
        
    db_etiqueta = Etiqueta(id_archivo = id_archivo1, etiqueta = jsonString, Usuario_id_usuario_id = usuarios_obj.id_usuario, caneca='Plastico')
    db_etiqueta.save()
    db_actividad = Actividad(Usuario_id_usuario_id = usuarios_obj.id_usuario, tipo_actividad = 'etiquetado')
    db_actividad.save()
    db_puntos = Puntos(cantidad_puntos = 5, Usuario_id_usuario_id = usuarios_obj.id_usuario)
    db_puntos.save()
    return render(request, 'exito_Etiquetado.html')
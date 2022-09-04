from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import Incentivos, Usuarios
from .forms import UploadImageForm
#from django.shortcuts import render_to_response, RequestContext

id2 = 1

def home(request):
    usuarios_obj = Usuarios.objects.get(id = id2)
    return render(request, 'home.html', {'nombre':usuarios_obj.nombre})

def mis_incentivos(request):
    usuarios_obj = Usuarios.objects.get(id = id2)
    incentivos = Incentivos.objects.get(id = id2)
    return render(request, 'mis_incentivos.html', {'nombre':usuarios_obj.nombre, 'codigo':usuarios_obj.codigo, 'puntos':incentivos.puntos})

def mi_actividad(request):
    usuarios_obj = Usuarios.objects.get(id = id2)
    incentivos = Incentivos.objects.get(id = id2)
    return render(request, 'mi_actividad.html', {'nombre':usuarios_obj.nombre, 'codigo': usuarios_obj.codigo, 'cantidadRecogida':usuarios_obj.cantidadRecogida, 'puntos': incentivos.puntos})

def filtrar_por(request):
    return render(request, 'filtrar_por.html')

def etiquetado(request):
    return render(request, 'etiquetado.html')

"""def upload_image_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Image uploaded succesfully!"
    else:
        form = UploadImageForm()

    return render_to_response('albums/upload.html', locals(), context_instance=RequestContext(request))"""

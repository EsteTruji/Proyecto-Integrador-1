"""EcoMind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_1 import views as app1Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1Views.home),
    path('mis_incentivos/', app1Views.mis_incentivos),
    path('mi_actividad/', app1Views.mi_actividad),
    path('filtrar_por/', app1Views.filtrar_por),
    path('etiquetado/', app1Views.etiquetado),
]

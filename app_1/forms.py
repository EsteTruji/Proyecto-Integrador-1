from django import forms
#from .models import etiqueta

class UploadImageForm(forms.ModelForm):
    
    class Meta:
        #model = etiqueta
        fields = ['carpeta', 'img']
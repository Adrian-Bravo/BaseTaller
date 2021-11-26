from django import forms
from django.forms import fields, widgets
from django.forms.fields import Field
from apps.fabricantes.models import Fabricantes
class fabricanteForm(forms.ModelForm):
    class Meta:
        model =Fabricantes
        fields = [
            'nombre',
            'domicilio',
            'componentes'
        ]
        labels = {
            'nombre':'Nombre',
            'domicilio':'Domicilio',
            'componentes':'Componentes'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'componentes': forms.TextInput(attrs={'class': 'form-control'}),
            #'tipoClient':forms.Select(attrs={'class': 'form-control'}),
        }

from django import forms
from django.forms import fields, widgets
from apps.componentes.models import Componentes

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componentes

        fields = [
            'nombre',
            'especificaciones',
            'cantidad',
            'precio',
            'aparatos',
        ]

        labels = {
            'nombre': 'Nombre',
            'especificaciones': 'Especificaciones',
            'cantidad': 'Cantidad',
            'precio': 'Precio',
            'aparatos': 'Aparatos',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'especificaciones': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'aparatos': forms.Select(attrs={'class': 'form-control'}),
        }
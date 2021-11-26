from django import forms
from django.forms import fields, widgets
from apps.componentes.models import Componentes
from apps.tipo_elec.models import Tipos_elec

class TeForm(forms.ModelForm):
    class Meta:
        model = Tipos_elec

        fields = [
            'nombre',
            'caracteristicas',
            'aparatos',
        ]

        labels = {
            'nombre': 'Nombre',
            'caracteristicas': 'Caracteristicas',
            'aparatos': 'Aparatos',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'caracteristicas': forms.TextInput(attrs={'class': 'form-control'}),
            'aparatos': forms.Select(attrs={'class': 'form-control'}),
        }
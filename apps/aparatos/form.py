from django import forms
from django.forms import fields, widgets
from apps.aparatos.models import Aparatos

class AparatoForm(forms.ModelForm):
    class Meta:
        model = Aparatos

        fields = [
            'descripcion',
        ]

        labels = {
            'descripcion': 'Descripcion'
        }

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }
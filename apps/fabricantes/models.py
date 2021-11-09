from django.db import models
from apps.componentes.models import Componentes

# Create your models here.

class Fabricantes(models.Model):
    nombre = models.CharField(max_length=60)
    domicilio = models.CharField(max_length=200)
    componentes = models.ForeignKey(Componentes, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

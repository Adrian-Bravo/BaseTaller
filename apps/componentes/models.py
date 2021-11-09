from django.db import models
from apps.aparatos.models import Aparatos

# Create your models here.

class Componentes(models.Model):
    nombre = models.CharField(max_length=60)
    especificaciones = models.CharField(max_length=300)
    cantidad = models.IntegerField(default=0)
    precio = models.BigIntegerField()
    aparatos = models.ForeignKey(Aparatos, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
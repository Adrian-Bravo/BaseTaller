from django.db import models
from apps.aparatos.models import Aparatos
# Create your models here.
class Tipos_elec(models.Model):
    nombre = models.CharField(max_length=60)
    caracteristicas = models.TextField()
    aparatos = models.ForeignKey(Aparatos, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
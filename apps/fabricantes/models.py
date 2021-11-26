from django.db import models


# Create your models here.

class Fabricantes(models.Model):
    nombre = models.CharField(max_length=60)
    domicilio = models.CharField(max_length=200)
    componentes = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

from django.db import models

class Aparatos(models.Model):
    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.descripcion
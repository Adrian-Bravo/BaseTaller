from django.contrib import admin
from apps.fabricantes.models import Fabricantes

# Register your models here.
class fabricantesAdmin (admin.ModelAdmin):
    
    list_display =('nombre','domicilio','componentes')
    ordering =('nombre','domicilio','componentes')
    search_fields =('nombre','domicilio')

admin.site.register(Fabricantes)

from django.urls import path, include

from apps.aparatos.views import aparatoCreate, aparatoEdit, aparatoEliminar, index


app_name = "aparatos"

urlpatterns = [
    path('', index, name='index'),
    path('crear/', aparatoCreate, name='aparatoCreate'),
    path('actualizar/<int:id_aparato>', aparatoEdit, name='aparatoEdit'),
    path('eliminar/<int:id_aparato>', aparatoEliminar, name='aparatoEliminar'),
]
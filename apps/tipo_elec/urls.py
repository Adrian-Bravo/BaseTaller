from django.urls import path, include
from apps.tipo_elec.views import TeCreate, TeEdit, TeEliminar, index

app_name = "tipos_ele"

urlpatterns = [
    path('', index, name='index'),
    path('crear/', TeCreate, name='teCreate'),
    path('actualizar/<int:id_te>', TeEdit, name='teEdit'),
    path('eliminar/<int:id_te>', TeEliminar, name='teEliminar'),
]
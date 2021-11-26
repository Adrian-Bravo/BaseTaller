from django.urls import path, include
from apps.componentes.views import componentesEliminar, index, componentesCreate, componentesEdit

app_name = "componentes"

urlpatterns = [
    path('', index, name='index'),
    path('crear/', componentesCreate, name='componentesCreate'),
    path('actualizar/<int:id_componente>', componentesEdit, name='componentesEdit'),
    path('eliminar/<int:id_componente>', componentesEliminar, name='componentesEliminar'),
]
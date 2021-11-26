from django.urls import path, include
from apps.componentes.views import index

app_name = "componentes"

urlpatterns = [
    path('', index, name='index'),
    path('crear/', componentesCreate, name='componentesCreate'),
]
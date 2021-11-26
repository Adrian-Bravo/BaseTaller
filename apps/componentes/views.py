from django.shortcuts import render

from apps.componentes.models import Componentes

# Create your views here.

def index(request):
    componente = Componentes.objects.all()
    context = {'componentes': componente}
    return render (request,'componentes/index.html',context)

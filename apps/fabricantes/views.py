from django.shortcuts import render
from django.http import HttpResponse
from apps.fabricantes.models import Fabricantes

# Create your views here.
def index (request):
    fabricantes = Fabricantes.objects.all().order_by('-id')
    context ={'fabricantes': fabricantes}
    return render (request,'fabricantes/index.html',context)
    # return render(request,'fabricantes/index.html')
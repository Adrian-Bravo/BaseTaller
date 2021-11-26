from django.shortcuts import render,redirect

from apps.fabricantes.form import fabricanteForm
from apps.fabricantes.models import Fabricantes

# Create your views here.  
def index (request):
    fabricantes = Fabricantes.objects.all().order_by('id')
    context ={'fabricantes': fabricantes}
    return render (request,'fabricantes/index.html',context)
    # return render(request,'fabricantes/index.html')

def fabricanteCreate(request):
        if (request.method =='POST'):
            form =fabricanteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('fabricantes:index')
        else:
            form =fabricanteForm()
            return render(request,'fabricantes/formFabricante.html',{'form': form})

def fabricanteEdit(request, id_fabricante):
    fabricante= Fabricantes.objects.get(pk=id_fabricante)
    if (request.method =='GET'):
        form =fabricanteForm(instance= fabricante)
    else:
        form =fabricanteForm(request.POST,instance=fabricante)
        if  form.is_valid():
            form.save()
        return redirect ('fabricantes:index')
    return render(request,'fabricantes/formFabricante.html',{'form':form})

def fabricanteEliminar (request, id_fabricante):
    fabricante= Fabricantes.objects.get(pk=id_fabricante)
    if request.method =='POST':
        fabricante.delete()
        return redirect ('fabricantes:index')
    return render(request, 'fabricantes/fabricanteEliminar.html',{'fabricante':fabricante})
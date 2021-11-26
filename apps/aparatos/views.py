from django.shortcuts import redirect, render
from apps.aparatos.models import Aparatos
from apps.aparatos.form import AparatoForm

# Create your views here.

def index(request):
    aparato = Aparatos.objects.all()
    context = {'aparatos': aparato}
    return render (request,'aparatos/index.html',context)

def aparatoCreate(request):
    if(request.method == 'POST'):
        form = AparatoForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('aparatos:index')
    else:
        form = AparatoForm()
        return render(request, 'aparatos/formAparato.html', {'form': form})


def aparatoEdit(request, id_aparato):

    aparato = Aparatos.objects.get(pk=id_aparato)
    if(request.method == 'GET'):
        form = AparatoForm(instance=aparato)
    else:
        form = AparatoForm(request.POST, instance=aparato)
        if form.is_valid():
            form.save()

        return redirect('aparatos:index')

    return render(request, 'aparatos/formAparato.html', {'form': form})


def aparatoEliminar(request, id_aparato):

    aparato = Aparatos.objects.get(pk=id_aparato)

    if(request.method == 'POST'):
        aparato.delete()
        return redirect('aparatos:index')

    return render(request, 'aparatos/aparatoEliminar.html', {'aparato': aparato})
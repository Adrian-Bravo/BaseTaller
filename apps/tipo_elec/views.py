from django.shortcuts import redirect, render
from apps.tipo_elec.form import TeForm
from apps.tipo_elec.models import Tipos_elec

# Create your views here.

def index(request):
    te = Tipos_elec.objects.all()
    context = {'tes': te}
    return render (request,'tipos_ele/index.html',context)

def TeCreate(request):
    if(request.method == 'POST'):
        form = TeForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('tipos_ele:index')
    else:
        form = TeForm()
        return render(request, 'tipos_ele/formTe.html', {'form': form})

def TeEdit(request, id_te):
    te = Tipos_elec.objects.get(pk=id_te)
    if(request.method == 'GET'):
        form = TeForm(instance=te)
    else:
        form = TeForm(request.POST, instance=te)
        if form.is_valid():
            form.save()

        return redirect('tipos_ele:index')

    return render(request, 'tipos_ele/formTe.html', {'form': form})


def TeEliminar(request, id_te):
    te = Tipos_elec.objects.get(pk=id_te)
    if(request.method == 'POST'):
        te.delete()
        return redirect('tipos_ele:index')

    return render(request, 'tipos_ele/teEliminar.html', {'te': te})

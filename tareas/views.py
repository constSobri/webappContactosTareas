from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm

# Create your views here.
def tareas(request):
    tareas = Tarea.objects.all()
    
    context = {'tareas':tareas}
    
    return render(request, 'tareas.html', context)

def tareas_create(request):
    if request.method == 'POST':
        formulario = TareaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tareas')
    else:
        formulario = TareaForm()
    return render(request, 'tareas_create.html', {'formulario': formulario})

def tarea_detail(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    return render(request, 'tarea_detail.html', {'tarea': tarea})

def tarea_edit(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    
    if request.method == 'POST':
        formulario = TareaForm(request.POST, instance=tarea)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarea_detail', id=id)
    else:
        formulario = TareaForm(instance=tarea)
    
    return render(request, 'tarea_edit.html', {'formulario': formulario})

def tarea_remove(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.delete()
    return redirect('tareas')

def filtrado_por_letra(request, letra):
    tareas = Tarea.objects.filter(name__istartswith=letra)
    context = {
        'tareas': tareas,
    }
    return render(request, 'tareas.html', context)
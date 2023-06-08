from django.shortcuts import render, get_object_or_404, redirect
from .models import Contacto
from .forms import ContactoForm

# Create your views here.
def contactos(request):
    contactos = Contacto.objects.all()
    
    context = {'contactos':contactos}
    
    return render(request, 'contactos.html', context)

def contactos_create(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('contactos')
    else:
        formulario = ContactoForm()
    return render(request, 'contactos_create.html', {'formulario': formulario})

def contactos_detail(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    return render(request, 'contactos_detail.html', {'contacto': contacto})

def contactos_edit(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    
    if request.method == 'POST':
        formulario = ContactoForm(request.POST, instance=contacto)
        if formulario.is_valid():
            formulario.save()
            return redirect('contactos_detail', id=id)
    else:
        formulario = ContactoForm(instance=contacto)
    
    return render(request, 'contactos_edit.html', {'formulario': formulario})

def contactos_remove(request, id):
    contacto = Contacto.objects.get(id=id)
    contacto.delete()
    return redirect('contactos')

def filtrado_por_letra(request, letra):
    contactos = Contacto.objects.filter(name__istartswith=letra)
    context = {
        'contactos': contactos,
    }
    return render(request, 'contactos.html', context)
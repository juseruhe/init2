from init2.aplicaciones.principal.forms import PersonaForm
from django.shortcuts import redirect, render

from .models import Persona

# Create your views here.

def inicio(request):
    personas = Persona.objects.all()
    datos = {'personas': personas}
    return render(request,'index.html',datos)


def create(request):
    form = PersonaForm()
    formulario = {
        'form' : form
    }
    return render(request,'crear_persona.html',formulario)

def store(request):
     form = PersonaForm(request.POST)
     if form.is_valid():
         form.save()
     return redirect('index')
 
 
def show(request,id):
    persona =  Persona.objects.get(id = id)
    datos = {
        "persona": persona
    }
        
    return render(request,'mostrar.html',datos)



def edit(request,id):
    persona =  Persona.objects.get(id = id)
 
    datos = {
        "persona": persona
    }
    return render(request,'editar.html',datos)


def update(request,id):
    persona = Persona.objects.get(id = id)
    form = PersonaForm(request.POST,instance=persona)
    if form.is_valid:
        form.save()
    return redirect('show',id)

def destroy(request,id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('index')

    
    


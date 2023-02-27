from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import sitios
from .forms import sitios_form

# Create your views here.

def sites(request):
    return render (request, 'sites.html')

def selectsite(request):
    return render (request, 'selectsite.html')

def listsite(request):
    datos = sitios.objects.all
    return render (request, 'listsite.html', {'sitios': datos})

def delete(request, id):
    sitio = sitios.objects.get(id=id)
    sitio.delete()
    return redirect('listsite')

def nuevo(request):
    formulario = sitios_form(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('listsite')
    return render(request, 'createsite.html', {'formulario': formulario})
    
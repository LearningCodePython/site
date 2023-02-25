from django.shortcuts import render
from django.http import HttpResponse
from .models import sitios

# Create your views here.

def sites(request):
    return render (request, 'sites.html')

def selectsite(request):
    return render (request, 'selectsite.html')

def listsite(request):
    datos = sitios.objects.all
    return render (request, 'listsite.html', {'sitios': datos})

def deletesite(request):
    return render (request,'deletesite.html')

def nuevo(request):
    return render (request,'createsite.html')
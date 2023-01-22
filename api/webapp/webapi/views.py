from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sites(request):
    return render (request, 'sites.html')

def selectsite(request):
    return render (request, 'selectsite.html')

def listsite(request):
    return render (request, 'listsite.html')

def deletesite(request):
    return render (request,'deletesite.html')

def createsite(request):
    return render (request,'createsite.html')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sites(request):
    return render (request, 'sites.html')
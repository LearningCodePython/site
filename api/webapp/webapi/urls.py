from django.urls import path
from . import views

urlpatterns = [
    path('sites', views.sites, name='sites'),
    path('selectsite', views.selectsite, name='selectsite'),
    path('listsite', views.listsite, name='listsite'),
    path('deletesite', views.deletesite, name='deletesite'),
    path('nuevo', views.nuevo, name='nuevo'),
]


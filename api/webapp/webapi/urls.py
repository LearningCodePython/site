from django.urls import path
from . import views

urlpatterns = [
    path('', views.sites, name='sites'),
    path('sites', views.sites, name='sites'),
    path('selectsite', views.selectsite, name='selectsite'),
    path('listsite', views.listsite, name='listsite'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('nuevo', views.nuevo, name='nuevo'),

]


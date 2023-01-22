from django.contrib import admin

# Register your models here.
from .models import sitios, vpn_data


admin.site.register(sitios) 
admin.site.register(vpn_data)
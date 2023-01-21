from django.db import models

# Create your models here.

class sitios(models.Model):
    nombre = models.CharField(max_length=50)
    host = models.CharField(max_length=50)
    api_password = models.CharField(max_length=50)
    api_user = models.CharField(max_length=50)

    def __str__(self):
    	fila = self.nombre
    	return fila
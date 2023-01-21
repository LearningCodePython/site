[[Canva guia.canvas]]
[[Python Code]]
[[CSS Code]]
[[HTML Code]]

# Crear un proyecto.
 
Siguiendo la [[Guia - Entorno de Trabajo -.]], podemos instalar el framework Django para aplicaciones web

1. Crear una estructura dentro de nuestro proyecto de Python. ^bde018
```bash
$ django-admin startproject <nombre_de_poryecto>
```
`nombre_de_proyecto`: Es el nombre del proyecto Django en mi caso yo uso _webapp_ quedando la orden como sigue:

* Ejemplo.
```bash
$ django-admin startproject webapp
```

^44b671

- Django creará una carpeta dentro de nuestro proyecto (o sistema) con una serie de archivos. Esta carpeta sera la carpeta del sistema o general.

```bash
└── webapp
	└──webapp
		    ├── __init__.py
		    ├── asgi.py
		    ├── manage.py
		    ├── settings.py
		    ├── urls.py
		    └── wsgi.py
	
```
2. __Crear una app__
```bash
$ python3 manage.py startapp <app_name>
```
`app_name`: Es el nombre de la app o sitio web yo usaré como nombre de la app _yeastar_ quedando la orden como sigue: 

* Ejemplo.
```bash
$ python3 manage.py startapp yeastar
```

Esta orden crea un nuevo directorio dentro del directorio sistema, 

```bash
└── webapp
	└──webapp
	└──yeastar
		├── admin.py
		├── apps.py
		├── __init__.py
		├── models.py
		├── tests.py
		├── urls.py
		└── views.py
```

# Servidor.
1. Para levantar el servidor Django usamos el comando, que permite acceder a la aplicación web usamos el comando:

```bash
$ python namage.py runserver
```

## Ficheros importantes:
```shell
/Sistema/proyecto/settings.py
/Sistema/proyecto/urls.py
/Sistema/proyecto/__init__.py

/Sistema/app/views.py
/Sistema/app/urls.py
/Sistema/app/models.py
/Sistema/app/admin.py


```
 ***
### Carpeta del Proyecto o configuración general.
_settings.py_
- Dentro del fichero _setting.py_ que esté dentro del proyecto de django que hemos creado [[Guia Django#^44b671]]debemos declarar las aplicaciones que nosotros creamos, en este caso es _yeastar_ , quedando de esta manera.
![[setting_01.png]]

__settings.py__  Debe incluir los datos de la conexión al servidor MySQL y las app que has instalado
```python
.
.
.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapi' # Nuenva app
]

.
.
.
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # usamos mysql
        'NAME': 'API', #Nombre de tu proyecto Web
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

__urls.py__ Del proyecto.
```python
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapi.urls')) #
]
```
`path('', include('webapi.urls'))`: Se añade el path a nuestro proyecto web con Django en este caso está apuntando al fichero _urls.py_ del proyecto _webapp_

__init.py__ Del proyecto.
```python
import pymysql
pymysql.install_as_MySQLdb()
```

***
### Carpeta del Website o app

__urls.py__ De la app.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sites, name='sites'),
]

```

__views.py__ De la app.
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sites(request):
    return render (request, 'sites.html')

```

***

__models.py__ De la app.
```python
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
```

__admin.py__ De la app.
```python
from django.contrib import admin

# Register your models here.
from .models import sitios


admin.site.register(sitios)
```
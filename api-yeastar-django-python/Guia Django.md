[[Canva guia.canvas]]
[[Python Code]]
[[CSS Code]]
[[HTML Code]]
# Crear.
Siguiendo la [[Guia - Entorno de Trabajo -.]], podemos instalar el framework Django para aplicaciones web

1. Crear una estructura dentro de nuestro proyecto de Python. ^bde018
```bash
$ django-admin startproject <nombre_de_poryecto>
```
`nombre_de_proyecto`: Es el nombre del proyecto Django en mi caso yo uso _webapp_ quedando la orden como sigue:

```bash
$ django-admin startproject webapp
```

^44b671

- Django creará una carpeta dentro de nuestro proyecto python con una serie de archivos.
```bash
webapp
    ├── __init__.py
    ├── asgi.py
    ├── manage.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
	
```
2. Crear una app
```bash
$ python3 manage.py startapp <app_name>
```
`app_name`: Es el nombre de la app y usaré como nombre de la app _yeastar_ quedando la orden como sigue: 
```bash
$ python3 manage.py startapp yeastar
```
Esta orden crea un nuevo directorio dentro del directorio API, 
```bash
yeastar
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

# Servidor.
1. Para levantar el servidor Django usamos el comando.
```bash
$ python namage.py runserver
```

_settings.py_
- Dentro del fichero _setting.py_ que esté dentro del proyecto de django que hemos creado [[Guia Django#^44b671]]debemos declarar las aplicaciones que nosotros creamos, en este caso es _yeastar_ , quedando de esta manera.
![[setting_01.png]]
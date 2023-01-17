# Preparar entorno de programación.
Usaré el lenguaje de programación *python* en su versión 3, pero siguiendo las recomendaciones trabajaré en entorno virtualizado. Como IDLE usaré *Visual Studio Code*, y como framework *Django*, en la programación html intentaré alejarme de Bootstrap la mas posible de manera que usaré *CSS*. Ademas como la intención de este proyecto es crear un entorno de gestión varias centrales o "sites" necesitaré almacenar datos en bases de datos por los que usaré Mysql-Server pero en este caso este servidor de bases de datos estará en un contenedor Docker.

Esta primera parte del proyecto seguirá esta hoja de ruta.
1. [[Guia - Entorno de Trabajo -.#Instalar Python.]]
	1.[[Guia - Entorno de Trabajo -.#^f600a6]]
3. [[Guia - Entorno de Trabajo -.#Instalar Docker.]] 
4. [[Guia - Entorno de Trabajo -.#Crear un Contenedor como servidor MySql]]
	1. Por linea de comando.[[Guia - Entorno de Trabajo -.#^52d2a7]]
	2. Usando docker-file.[[Guia - Entorno de Trabajo -.#^d5e00d]]
4. [[Guia - Entorno de Trabajo -.#Instalar Visual Studio Code.]]
5. [[Guia - Entorno de Trabajo -.#Instalar el Framework Django.]]

## Instalar Python.

```bash
$ sudo apt-get update
$ sudo apt-get install python3.8
```

### Activar/Crear entorno Virtualizado.

^f600a6

1. Instalar pip

```bash
$ sudo apt install -y python3-pip
```
2. Instalar los paquetes de herramientas adicionales
```bash
$ sudo apt install build-essential libssl-dev libffi-dev python3-dev
```
3. Instalar virtuales. 
```bash
$ sudo apt install -y python3-venv
```
4. Crear un entorno virtual. Para este ejemplo #mi_entorno sera el nombre que queramos darle a nuestro entorno , es recomendable asignarle un nombre relacionado con el proyecto.
```bash
$ python3.6 -m venv mi_entorno
```
6. Activar un entorno virtual de este ejemplo el entorno virtual usado es #mi_entorno  ^a797d3
```bash
$ source mi_entorno/bin/activate mi_entorno.
```
7. Al finalizar el trabajo podemos desactivar el entrono con el comando *deactivate*
```bash
(mi_entorno) user@mipc:~/enviroment_path$ deactivate 
```
## Instalar Docker.

[link a la ayuda en linea](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-es)

1. Primero añadimos las fuentes APT los repositorios de Docker

```bash
$ sudo apt update
$ sudo apt install apt-transport-https ca-certificates curl software-properties-common # Paquetes de requisitos previos.
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - # Añadimos la clave GPG del repositorio de Docker
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable" #Agregar el repositorio de Docker a las fuestes APT
$ sudo apt update
$ sudo apt install docker-ce
```

2. Comprobar el funcionamiento del demonio.
```bash
$ sudo systemctl status docker
```
3. Para ejecutar docker sin _sudo_
```bash
$ sudo usermod -aG docker ${USER}
```
4. Aplicar la nueva membresía hay que cerrar la sesión del servidor y volver a iniciar.
```bash
$ su - ${USER}
```
5. Confirmar que el usuario se ha añadido al grupo `docker`
```bash
$ id -nG
```
6. Si debe agregar al grupo `docker` un usuario con el que no inició sesión, declare dicho nombre de usuario de forma explícita usando lo siguiente
```bash
$ sudo usermod -aG docker <username>
```
7. Comprobar que docker esta instalado.
```hash
$ docker --version
```
## Crear un Contenedor como servidor MySql
### Sin persistencia.

^52d2a7

```
docker run -d --rm --name mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 mysql:8.0
```
docker run -d --rm --name mysql -e MYSQL_ROOT_PASSWORD=`root` -p 3306:3306 mysql:8.0 Ejecutando esta linea de comandos simplemente cambiando la variable `MYSQL_ROOT_PASSWORD`por el valor que deseemos podemos ejecutar un contenedor con un MYSQL-SERVER en su version 8.0. Pero esta opción solo es valida si no queremos almacenar o mantener las modificaciones que se hagan, es valido para el desarrollo, pero no para usarlo en el futuro
-   `docker run` es el comando que nos permite crear un contenedor a partir de una imagen Docker.
    
-   El parámetro `-d` nos permite ejecutar el contenedor en modo _detached_, es decir, ejecutándose en segundo plano.
    
-   El parámetro `--rm` hace que cuando salgamos del contenedor, éste se elimine y no ocupe espacio en nuestro disco.
    
-   El parámetro `--name` nos permite asignarle un nombre a nuestro contenedor. Si no le asignamos un nombre [Docker](https://www.docker.com) nos asignará un nombre automáticamente.
    
-   El parámetro `e` es para pasarle al contenedor una variable de entorno. En este caso le estamos pasando la variable de entorno `MYSQL_ROOT_PASSWORD` con el valor de la contraseña que tendrá el usuario `root` para MySQL Server.
    
-   El parámetro `-p` nos permite mapear los puertos entre nuestra máquina local y el contenedor. En este caso, estamos mapeando el puerto `3306` de nuestra máquina local con el puerto `3306` del contenedor.
    
-   `mysql:8.0` es el nombre de la imagen y la versión que vamos a utilizar para crear el contenedor. Si no se indica lo contrario buscará las imágenes en el repositorio oficial [Docker Hub](https://hub.docker.com).

### Con persistencia de datos.

^d5e00d

Docker nos ofrece dos posibilidades para implementar persistencia de datos en los contenedores:

-   `bind mount`: pueden estar almacenados en cualquier directorio del sistema de archivos de la máquina host. Estos archivos pueden ser consultados o modificados por otros procesos de la máquina host o incluso por otros contenedores Docker.
    
-   `volume`: se almacenan en la máquina host dentro del área del sistema de archivos que gestiona Docker. Otros procesos de la máquina host no deberían modificar estos archivos, sólo deberían ser modificados por contenedores Docker.

Uso del parámetro `-v` para crear un volumen de tipo `bind_mount`:

```
-v /home/<user_directory>/data:/var/lib/mysql
```
Uso del parámetro `-v` para crear un volumen de tipo `bind_mount` con la variable de entorno `$PWD`:
```
-v "$PWD":/var/lib/mysql
```

* Esta seria la orden que debemos usar para usando el modo `bind_mount` Recuerda borrar el parámetro `--rm`si quieres que el contenedor no se borre al salir.
```bash
docker run -d --rm --name mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -v "$PWD":/var/lib/mysql mysql:8.0
```
***
Uso del parámetro `-v` con un volumen de tipo `volume`:
```
-v mysql_data:/var/lib/mysql
```

* Esta seria la orden que deberiamos usar en nuestra consola usando `volumen`. Recuerda borrar el parámetro `--rm`si quieres que el contenedor no se borre al salir.
```bash
docker run -d --rm --name mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -v mysql_data:/var/lib/mysql mysql:8.0
```
***
## Instalar Visual Studio Code.
[Link a la ayuda](https://es.linuxcapable.com/c%C3%B3mo-instalar-visual-studio-code-vs-code-en-linux-mint-20/)

```bash
$ sudo apt update && sudo apt upgrade -y
```

Los siguientes paquetes deben instalarse para ayudar en la instalación del software.

```bash
$ sudo apt install software-properties-common apt-transport-https wget -y
```

Importar la clave GPG de Microsoft para verificar la autenticidad del paquete de instalación.

```bash
$ sudo wget -O- https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor | sudo tee /usr/share/keyrings/vscode.gpg
```

Importe el Repositorio de Microsoft Visual Source con el siguiente comando en su terminal.

```bash
$ echo deb [arch=amd64 signed-by=/usr/share/keyrings/vscode.gpg] https://packages.microsoft.com/repos/vscode stable main | sudo tee /etc/apt/sources.list.d/vscode.list
```

```bash
$ sudo apt update
$ sudo apt install code -y
$ sudo apt install code-insiders -y
```
## Instalar el Framework Django.
[[Guia Django]]
Para instalar Django usamos el comando pip3 instalado en el primer paso, esta herramienta nos ayuda a instalar paquetes de Python.
```bash
$pip3 install Django==4.1.5
```
Es este caso usamos la versión 4.1.5 puedes ir a la documentación oficial de Django [aqui](https://www.djangoproject.com/)

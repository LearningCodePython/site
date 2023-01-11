# Inicio db Code.
- Crear la conexión con el servidor de bases de datos MySql creado en [[Guia - Entorno de Trabajo -.#Crear un Contenedor como servidor MySql]] ^c5cc58

- Desde un solo fichero y para acelerar las pruebas se crea la base de datos y la tabla site donde se almaneca la información de acceso a la API de cada unos de los clientes. [[inicio.py]] ^7c0e24

# Inicio API conexción.
- Crear la conexión con la API.
	- El primer paso del proyecto es usar las variables locales y posteriormente usar las variables extraídas de la base de datos.
	- Para establecer la conexión con la central necesito:
		- ip de la central:
		- usuario de la API:
		- password de la API: en formato MD5
	- Esta informacion y haciendo una solicitud vis POST recogeremos un token que debemos almacenar para futuras conexiones.
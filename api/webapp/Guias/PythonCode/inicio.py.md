# Debemos crear la la structura de la base de datos primero.
* Ejecutaremos el siguieten comando que creara una base de datos (elegiremos "API") y dentro de esta base de datos creara una tabla llamada "site"

```bash
(api) emilio@cremheda:~/Codigo/site/api/webapp$ python inicio.py
```

[[Python Code#^7c0e24]]
```python
import mysql.connector
from conector import cursor

db_name=input("Primero crearemos la base de datos. Que nombre le daremos?... ")

def createdb(name=db_name):
	cursor.execute(f"CREATE DATABASE {name}")
createdb()

def create_table_site():
	cursor.execute (f"CREATE TABLE {db_name}.site \
	(id INT AUTO_INCREMENT PRIMARY KEY, \
	nombre VARCHAR(20), \
	host VARCHAR(20), \
	api_password VARCHAR(45), \
	api_user VARCHAR(45))")

create_table_site()

print (f'He finalizado ya está creada la base de datos {db_name} y tambien he creado la \n tabla site donde se almacenan los datos de los clientes')

cursor.close()
```

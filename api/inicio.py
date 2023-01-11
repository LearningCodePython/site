import mysql.connector
from db_conector import cursor

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
from db_conector import cursor, mydb

def mycommit():
	mydb.commit()
	cursor.close()
    
def create_db(name):
	"""Crear una base de datos

	Args:
		name (str): Nombre de la Base de Datos o Schema
	"""
	cursor.execute(f"CREATE DATABASE {name}")
	cursor.close()

def drop_db(name):
	"""Borra una base de datos completa

	Args:
		name (str): Nombre de la Base de datos a borrar
	"""
	cursor.execute(f"DROP DATABASE {name}")
	cursor.close()

def setting_db():
	cuestion1=input("Quiere crear una base de datos? y/n ")
	cuestion2=input("Quiere borrar unabase de datos? y/n ")

	if cuestion1 == "y":
		dbname=input("Nombre de la base de Datos: ")
		create_db(dbname)
		print (f"Ha sido creada la base de datos {dbname} ")
	if cuestion2 == "y":
		dropname=input("Nombre de la base de Datos que quiere borrar. ")
		drop_db(dropname)
		print (f"Ha sido eliminada la base de datos {dropname}")
	if cuestion2 == "n" or cuestion1 == "n":
		print ("Adios")
	if cuestion1 == "n" and cuestion2 == "n":
		print ("Entonces no puedo hacer nada por ti. ")
	mycommit()
create_db("API")
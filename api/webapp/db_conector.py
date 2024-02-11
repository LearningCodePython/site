import mysql.connector

# Conectos usado posteriormente para acceder a la base de datos
# No se selecciona base de datos
mydb = mysql.connector.connect(
	 	host="localhost",
		user="root",
	  	password="root"
	)
cursor=mydb.cursor()




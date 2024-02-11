import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="API"
)
cursor=mydb.cursor()

################################################################################
# Función que devuelve el listado de las tablas de la base de datos mydb.database
def list_of_table():
    cursor=mydb.cursor()
    tables="SHOW FULL TABLES"
    cursor.execute(tables)
    for (tables) in cursor:
        print(tables[0])
    cursor.close()

################################################################################
# Función que devuelve el listado de las columnas row de la tabla site
def colums_in_table():
    cursor=mydb.cursor()
    comando= (f"SHOW COLUMNS FROM site")
    cursor.execute(comando)
    for (comando) in cursor:
        print(comando[0])
    cursor.close()

################################################################################
# Función que devuelve el listado de los elemntos almacenados en una tabla:    
def getAllRows():
    cursor.execute("SELECT * FROM site")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)


## Llamada a as funciones creadas
getAllRows()        

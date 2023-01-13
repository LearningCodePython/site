import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="API"
)
cursor=mydb.cursor()
# Función que devuelve una lista de las bases de datos en el servidor
def getdblist():
    cursor=mydb.cursor()
    database="SHOW DATABASES"
    cursor.execute(database)
    for (database) in cursor:
        print(database[0])

################################################################################333
# Función que devuelve el listado de los elemntos almacenados en una tabla:

def getAllRows():
    cursor.execute("SELECT * FROM site")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)

# Llamada a la finción:   
getAllRows()
        

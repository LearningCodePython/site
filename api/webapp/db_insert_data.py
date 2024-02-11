import mysql.connector
import hashlib

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'API'
)
cursor=mydb.cursor()

database_name = "API"
table_name = "site"

def insert(name, host, user, password):
    #Encode password:
    p_encode = password.encode()
    h = hashlib.new("md5", p_encode)
    passwd = (h.hexdigest())
    #Seleccion de base de tados.
    cursor.execute(f'USE {database_name}')
    #Insertar en la base de datos.
    sql = (f'INSERT INTO {table_name} (nombre, host, api_password, api_user) VALUES (%s, %s, %s, %s)')
    values = (name, host, user, passwd)
    cursor.execute(sql, values)
    mydb.commit()
    mydb.close()

# incertar datos en la base de satos site
insert('test', '10.104.40.10', 'api', 'A2fOp23u')


from db_conector import cursor, mydb
import hashlib

def mycommit():
	mydb.commit()
	cursor.close()

def insert_data(site, host, password, user):
	"""_summary_

	Args:
		site (_str_): _Nombre del sitio_
		host (_str_): _IP de acceso_
		password (_str_): _Password de la api_
		user (_str_): _User de la api_
	"""
	p_encode = password.encode()
	h = hashlib.new("md5", p_encode)
	d_password = (h.hexdigest())
	sql = "INSERT INTO API.site (nombre, host, api_password, api_user) VALUES (%s, %s, %s, %s)"
	val =(site, host, d_password, user)
	cursor.execute(sql, val)
	mycommit()

def delete_site(nombre):
	"""Borra los datos de un site

	Args:
		nombre (str): Nombre del site a borrar.
	"""
	sql = (f"DELETE FROM API.site WHERE nombre = '{nombre}'")
	cursor.execute(sql)
	commit()

def edit_name(a,n):
	"""Modifica el nombre de un site

	Args:
		a (str): Nombre actual de cliente o site
		n (str): Nuevo nombre de cliente o site
	"""
	sql = "UPDATE API.site SET nombre = %s WHERE nombre = %s"
	val = (n, a)
	cursor.execute(sql, val)
	mycommit()

def edit_host(a,n):
	"""Cambiar la IP de un site

	Args:
		a (str): Nombre de cliente
		n (str): Nueva direccion IP
	"""
	sql = "UPDATE API.site SET host = %s WHERE nombre = %s"
	val = (n, a)
	cursor.execute(sql, val)
	mycommit()

def edit_user(a,n):
	"""Cambia el user api

	Args:
		a (str): api_user actual
		n (str): api_user nuevo
	"""
	sql = "UPDATE API.site SET api_user = %s WHERE api_user = %s"
	val = (n, a)
	cursor.execute(sql, val)
	mycommit()

def edit_password(site_name,new_pass):
	"""Cambiar el password de acceso de un site

	Args:
		site_name (_str_): Nombre del site.
		new_pass (_str_): Nueva contraseña.
	"""
	p_encode = new_pass.encode()
	h = hashlib.new("md5", p_encode)
	password = (h.hexdigest())
	sql = "UPDATE API.site SET api_password = %s WHERE nombre = %s"
	val = (password, site_name)
	cursor.execute(sql, val)
	mycommit()

def selectrow():
	cursor.execute(f"SELECT nombre, host, api_password, api_user FROM API.site")
	myresultado = cursor.fetchall()
	for x in myresultado:
		print(x)
	cursor.close()

def select_site(name_s):
	"""_summary_

	Args:
		name_s (_str_): _Nombre del Site que quieres seleccionar_
	"""
	sql = (f"SELECT * FROM API.site WHERE nombre = '{name_s}'")
	cursor.execute(sql)
	resultado = cursor.fetchall()
	for x in resultado:
		f = open ('data.py', "w")
		f.write("site = \"% s\"" % x[1])
		f.write("\nhost = \"%s\""% x[2])
		f.write("\napi_password = \"\\\"% s\\\"\"" % x[3])
		f.write("\napi_user = \"\\\"% s\\\"\"" % x[4])
		f.close
	cursor.close()

################################
#####      TEST ZONE     #######
################################

# print(cursor.rowcount, "record(s) deleted")
# print (cursor.rowcount, "record(s) affected")


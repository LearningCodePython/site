[[Python Code#^c5cc58]]
```python
import mysql.connector
 
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="root"

)
cursor=mydb.cursor()
```

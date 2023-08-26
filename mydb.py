import mysql.connector

dataBase = mysql.connector.connect(
	host = '127.0.0.1',
	user = 'root',
	password = 'Mohit@3261900108'
	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE mohit")

print("All Done!")
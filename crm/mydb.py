import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Adity@02',
)

cursorObject = database.cursor()

cursorObject.execute('CREATE DATABASE IF NOT EXISTS CRM')

print('Database created successfully')
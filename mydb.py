#install my sql
#pip install mysql
#pip install mysql- connector
#pip install mysql-connector-pyhton

import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user= 'root',
    passwd= 'root'

)

#prepare a cursor object
cursorObject = dataBase.cursor()

#Create a datbase
cursorObject.execute("CREATE DATABASE crm_db")
print("ALL DONE!")
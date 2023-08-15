#Insatll mysql in computer
#pip install mysql
#pip install mysql-connector (as not working)
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Password123#@!"
    )

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE demoq_data_base")

print("All done!")
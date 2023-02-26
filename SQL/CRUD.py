import mysql.connector

try:
    dbcon = mysql.connector.connect(host="localhost", user="root", password="6301827563", database="pydata")
    dbcursor = dbcon.cursor()
    
    dbcursor.execute("create table employee3(id int, name varchar(32), email varchar(32), salary int)")
    print("Table Created")

except mysql.connector.Error as err:
    print('Unable to Establish Connection')
    print(err)
    
dbcon.close()
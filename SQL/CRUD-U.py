import mysql.connector

try:
    dbcon = mysql.connector.connect(host="localhost", user="root", password="6301827563", database="pydata")
    dbcursor = dbcon.cursor()

    dbcursor.execute("insert into employee3(id, name, email, salary) values(104, 'Surya', 'Surya@gmail.com', 155000)")
    print("Data Inserted")

    dbcon.commit()

    dbcursor.close()
    dbcon.close()
    
except mysql.connector.Error as err:
    print('Unable to Establish Connection')
    print(err)
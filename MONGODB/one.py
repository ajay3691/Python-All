import pymongo

#create monogo connection
client = pymongo.MongoClient()

#create Mongo database
mdb = client['pydata']

#create collection
mcol = mdb['emp']

mcol.insert_one({"id":101, "name":"Rahul"})

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  port = 8888, #for Mamp users
  database='whatever db you want'
)
print(mydb)
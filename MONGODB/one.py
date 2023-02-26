import pymongo

#create monogo connection
client = pymongo.MongoClient()

#create Mongo database
mdb = client['pydata']

#create collection
mcol = mdb['emp']

mcol.insert_one({"id":101, "name":"Rahul"})
import os;


from pymongo import MongoClient
conn = MongoClient('localhost', 27017)
#db
db = conn.digital
#db.a.insert_one({"mm":"lklk"})
collection = db.a
collection.insert_one({"yasmin":"yasmin"})

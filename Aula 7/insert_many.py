import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
    {"name": "Amy", "address": "Apple st 456"},
    {"name": "Hannah", "address": "Apple st 123"},
    {"name": "Michael", "address": "Apple st 000"},
    {"name": "Sandy", "address": "Apple st 999"},
    {"name": "Betty", "address": "Apple st 888"},
    {"name": "Richard", "address": "Apple st 777"},
    {"name": "Susan", "address": "Apple st 666"},
    {"name": "Vicky", "address": "Apple st 555"},
    {"name": "Ben", "address": "Apple st 444"},
    {"name": "Willian", "address": "Apple st 333"},
    {"name": "Chuck", "address": "Apple st 222"},
    {"name": "Viola", "address": "Apple st 111"},
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)

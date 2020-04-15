import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = {"nome": "Leonardo", "email": "leonardo@teste.com", "telefone": "16 99790 5755"}

x = mycol.insert_one(mydict)

print(x.inserted_id)

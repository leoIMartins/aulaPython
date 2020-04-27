import pymongo
# noinspection PyUnresolvedReferences
from Farmacia import Farmacia

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbatividade"]
mycolFarmacia = mydb["farmacia"]

farmacia = Farmacia()

while True:
    option = input("\n1 - Cadastrar farmácia\n"
                   "0 - Sair\n"
                   "Opção escolhida: ")

    if option == "1":
        farmacia.cadastrar_farmacia()

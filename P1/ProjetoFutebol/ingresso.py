import pymongo
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbfutebol"]
mycolIngresso = mydb["ingresso"]


def exibir_ingressos():
    ingressos_cadastradas = mycolIngresso.find()
    for c in ingressos_cadastradas:
        print(c)


class Ingresso:

    def __init__(self):
        self.preco = ""
        self.setor = ""
        
    def set_cpf(self, setor):
        self.setor = setor

    def set_nome(self, preco):
        self.preco = preco
    
    def get_cpf(self):
        return self.setor
    
    def get_nome(self):
        return self.preco

    def cadastrar_ingresso(self):
        quantidade = 0
        self.preco = input("Informe o preço do ingresso: ")
        self.setor = input("Informe o setor da arquibancada: ")
        while quantidade < 1:
            quantidade = int(input("Informe a quantidade a ser disponibilizada: "))
            if quantidade < 1:
                print("Informe uma quantidade maior que 0")
        for q in range(quantidade):
            ingresso = {"preco": self.preco, "setor": self.setor}
            mycolIngresso.insert_one(ingresso)

        return print("Ingresso(s) incluído(s) com sucesso!")

    @staticmethod
    def excluir_ingresso(tudo):
        mycolIngresso.delete_many({})
        return print("Ingresso(s) excluído(s) com sucesso!")

    @staticmethod
    def consultar_ingresso(tudo):
        exibir_ingressos()

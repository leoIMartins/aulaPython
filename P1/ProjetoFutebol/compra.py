import pymongo
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbfutebol"]
mycolCompra = mydb["compra"]


def exibir_compras():
    compras_cadastradas = mycolCompra.find()
    for c in compras_cadastradas:
        print(c)


class Compra:

    def __init__(self):
        self.jogo = ""
        self.setor = ""

    def set_cpf(self, setor):
        self.setor = setor

    def set_nome(self, jogo):
        self.jogo = jogo

    def get_cpf(self):
        return self.setor

    def get_nome(self):
        return self.jogo

    def cadastrar_compra(self):
        quantidade = 0
        self.jogo = input("Informe o preço do compra: ")
        self.setor = input("Informe o setor da arquibancada: ")
        while quantidade < 1:
            quantidade = int(input("Informe a quantidade a ser disponibilizada: "))
            if quantidade < 1:
                print("Informe uma quantidade maior que 0")
        for q in range(quantidade):
            compra = {"jogo": self.jogo, "setor": self.setor}
            mycolCompra.insert_one(compra)

        return print("Compra(s) incluído(s) com sucesso!")

    @staticmethod
    def excluir_compra(tudo):
        mycolCompra.delete_many({})
        return print("Compra(s) excluído(s) com sucesso!")

    @staticmethod
    def consultar_compra(tudo):
        exibir_compras()

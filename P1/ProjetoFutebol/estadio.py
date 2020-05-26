import pymongo
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbfutebol"]
mycolEstadio = mydb["estadio"]


def exibir_estadios():
    print("\n")
    for x in mycolEstadio.find():
        print("ID: %s" % x.get("_id"))
        print(" - Nome: %s" % x.get("nome"))
        print(" - País: %s" % x.get("pais"))
        print(" - Cidade: %s" % x.get("cidade"))
        print(" - Capacidade: %s" % x.get("capacidade"))
        print("----------------------------------------------------------------------------------------------")


class Estadio:

    def __init__(self):
        self.nome = ""
        self.pais = ""
        self.cidade = ""
        self.capacidade = ""

    def set_nome(self, nome):
        self.nome = nome

    def set_pais(self, pais):
        self.pais = pais

    def set_cidade(self, cidade):
        self.cidade = cidade

    def set_capacidade(self, capacidade):
        self.capacidade = capacidade

    def get_nome(self):
        return self.nome

    def get_pais(self):
        return self.pais

    def get_cidade(self):
        return self.cidade

    def get_capacidade(self):
        return self.capacidade

    def cadastrar_estadio(self):
        self.nome = input("Informe o nome do estádio: ")
        self.pais = input("Informe o país: ")
        self.cidade = input("Informe a cidade: ")
        self.capacidade = input("Informe a capacidade do estádio: ")
        estadio = {"nome": self.nome, "pais": self.pais, "cidade": self.cidade, "capacidade": self.capacidade}
        mycolEstadio.insert_one(estadio)
        return print("Estádio incluído com sucesso!")

    @staticmethod
    def alterar_estadio():
        exibir_estadios()
        estadio_escolhido = {"_id": ObjectId(input("Informe o ID do estádio a ser alterado: "))}
        atributo_escolhido = input("\nInforme o atributo (exatamente como está abaixo) a ser alterado no estádio:\n"
                                   "nome || pais || cidade || capacidade\n"
                                   "Atributo escolhido: ")

        novo_valor = {"$set": {atributo_escolhido: input("\nInforme o novo valor para o atributo: ")}}
        mycolEstadio.update_one(estadio_escolhido, novo_valor)
        return print("Estádio alterado com sucesso!")

    @staticmethod
    def excluir_estadio(tudo):
        if tudo:
            mycolEstadio.delete_many({})
            return print("Estádio(s) excluído(s) com sucesso!")
        else:
            exibir_estadios()
            mycolEstadio.delete_one({"_id": ObjectId(input("Informe o ID do estádio a ser excluído: "))})
            return print("Estádio excluído com sucesso!")

    @staticmethod
    def consultar_estadio(tudo):
        print("\n")
        if tudo:
            filtro = {}
        else:
            filtro = {input(
                "Informe o atributo (exatamente como está abaixo) do estadio a ser utilizado como"
                " parâmetro na consulta:\n"
                "nome || pais || cidade || capacidade\n"
                "Atributo escolhido: "): input("Informe o valor do atributo a ser pesquisado: ")}

        for x in mycolEstadio.find(filtro):
            print("ID: %s" % x.get("_id"))
            print(" - Nome: %s" % x.get("nome"))
            print(" - País: %s" % x.get("pais"))
            print(" - Cidade: %s" % x.get("cidade"))
            print(" - Capacidade: %s" % x.get("capacidade"))
            print("----------------------------------------------------------------------------------------------")

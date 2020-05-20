import pymongo
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbfutebol"]
mycolClube = mydb["clube"]


def exibir_clubes():
    clubes_cadastradas = mycolClube.find()
    for c in clubes_cadastradas:
        print(c)


class Clube:

    def __init__(self):
        self.nome = ""
        self.tecnico = ""
        self.numero_titulos = ""
        
    def set_tecnico(self, tecnico):
        self.tecnico = tecnico

    def set_nome(self, nome):
        self.nome = nome    

    def set_clube(self, clube):
        self.numero_titulos = clube
    
    def get_tecnico(self):
        return self.tecnico
    
    def get_nome(self):
        return self.nome

    def get_clube(self):
        return self.numero_titulos

    def cadastrar_clube(self):
        self.nome = input("Informe o nome do clube: ")
        self.tecnico = input("Informe o tecnico do clube: ")
        self.numero_titulos = input("Informe o numero de títulos do clube: ")
        clube = {"nome": self.nome, "tecnico": self.tecnico, "clube": self.numero_titulos}
        mycolClube.insert_one(clube)
        return print("Clube incluído com sucesso!")

    @staticmethod
    def alterar_clube():
        exibir_clubes()
        clube_escolhido = {"_id": ObjectId(input("Informe o ID do clube a ser alterado: "))}
        atributo_escollhido = input("\nInforme o atributo (exatamente como está abaixo) a ser alterado no clube:\n"
                                    "nome || tecnico || numero_titulos\n"
                                    "Atributo escolhido: ")

        novo_valor = {"$set": {atributo_escollhido: input("\nInforme o novo valor para o atributo: ")}}
        mycolClube.update_one(clube_escolhido, novo_valor)
        return print("Clube alterado com sucesso!")

    @staticmethod
    def excluir_clube(tudo):
        if tudo:
            mycolClube.delete_many({})
            return print("Clube(s) excluído(s) com sucesso!")
        else:
            exibir_clubes()
            mycolClube.delete_one({"_id": ObjectId(input("Informe o ID do clube a ser excluído: "))})
            return print("Clube excluído com sucesso!")

    @staticmethod
    def consultar_clube(tudo):
        if tudo:
            clubes_cadastrados = mycolClube.find()

            for c in clubes_cadastrados:
                print(c)

        else:
            filtro = {input(
                "\nInforme o atributo (exatamente como está abaixo) do clube a ser utilizado como"
                " parâmetro na consulta:\n"
                "nome || tecnico || numero_titulos\n"
                "Atributo escolhido: "): input("Informe o valor do atributo a ser pesquisado: ")}

            for c in mycolClube.find(filtro):
                print(c)

    @staticmethod
    def exibir_clubes():
        clubes_cadastrados = mycolClube.find()
        for c in clubes_cadastrados:
            print(c)

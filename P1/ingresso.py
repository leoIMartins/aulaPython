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
        self.preco = input("Informe o preço do ingresso: ")
        self.setor = input("Informe o setor do ingresso: ")
        ingresso = {"preco": self.preco, "setor": self.setor}
        mycolIngresso.insert_one(ingresso)
        return print("Ingresso incluído com sucesso!")

    @staticmethod
    def alterar_ingresso():
        exibir_ingressos()
        ingresso_escolhido = {"_id": ObjectId(input("Informe o ID do ingresso a ser alterado: "))}
        atributo_escollhido = input("\nInforme o atributo (exatamente como está abaixo) a ser alterado no ingresso:\n"
                                    "preco || setor\n"
                                    "Atributo escolhido: ")

        novo_valor = {"$set": {atributo_escollhido: input("\nInforme o novo valor para o atributo: ")}}
        mycolIngresso.update_one(ingresso_escolhido, novo_valor)
        return print("Ingresso alterado com sucesso!")

    @staticmethod
    def excluir_ingresso(tudo):
        if tudo:
            mycolIngresso.delete_many({})
            return print("Ingresso(s) excluído(s) com sucesso!")
        else:
            exibir_ingressos()
            mycolIngresso.delete_one({"_id": ObjectId(input("Informe o ID do ingresso a ser excluído: "))})
            return print("Ingresso excluído com sucesso!")

    @staticmethod
    def consultar_ingresso(tudo):
        if tudo:
            ingressos_cadastrados = mycolIngresso.find()

            for c in ingressos_cadastrados:
                print(c)

        else:
            filtro = {input(
                "\nInforme o atributo (exatamente como está abaixo) do ingresso a ser utilizado como"
                " parâmetro na consulta:\n"
                "preco || setor\n"
                "Atributo escolhido: "): input("Informe o valor do atributo a ser pesquisado: ")}

            for c in mycolIngresso.find(filtro):
                print(c)

    @staticmethod
    def exibir_ingressos():
        ingressos_cadastrados = mycolIngresso.find()
        for c in ingressos_cadastrados:
            print(c)

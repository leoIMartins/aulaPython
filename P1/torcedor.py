import pymongo
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbfutebol"]
mycolTorcedor = mydb["torcedor"]


def exibir_torcedores():
    torcedores_cadastradas = mycolTorcedor.find()
    for c in torcedores_cadastradas:
        print(c)


class Torcedor:

    def __init__(self):
        self.nome = ""
        self.cpf = ""
        self.time = ""
        self.idade = ""
        
    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_nome(self, nome):
        self.nome = nome    

    def set_idade(self, idade):
        self.idade = idade

    def set_time(self, time):
        self.time = time
    
    def get_cpf(self):
        return self.cpf
    
    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_time(self):
        return self.time

    def cadastrar_torcedor(self):
        self.nome = input("Informe o nome do torcedor: ")
        self.cpf = input("Informe o cpf do torcedor: ")
        self.time = input("Informe o endereço do torcedor: ")
        self.idade = input("Informe a idade do torcedor: ")
        torcedor = {"nome": self.nome, "cpf": self.cpf, "time": self.time, "idade": self.idade}
        mycolTorcedor.insert_one(torcedor)
        return print("Torcedor incluído com sucesso!")

    @staticmethod
    def alterar_torcedor():
        exibir_torcedores()
        torcedor_escolhido = {"_id": ObjectId(input("Informe o ID do torcedor a ser alterado: "))}
        atributo_escollhido = input("\nInforme o atributo (exatamente como está abaixo) a ser alterado no torcedor:\n"
                                    "nome || cpf || time || idade\n"
                                    "Atributo escolhido: ")

        novo_valor = {"$set": {atributo_escollhido: input("\nInforme o novo valor para o atributo: ")}}
        mycolTorcedor.update_one(torcedor_escolhido, novo_valor)
        return print("Torcedor alterado com sucesso!")

    @staticmethod
    def excluir_torcedor(tudo):
        if tudo:
            mycolTorcedor.delete_many({})
            return print("Torcedor(s) excluído(s) com sucesso!")
        else:
            exibir_torcedores()
            mycolTorcedor.delete_one({"_id": ObjectId(input("Informe o ID do torcedor a ser excluído: "))})
            return print("Torcedor excluído com sucesso!")

    @staticmethod
    def consultar_torcedor(tudo):
        if tudo:
            torcedores_cadastrados = mycolTorcedor.find()

            for c in torcedores_cadastrados:
                print(c)

        else:
            filtro = {input(
                "\nInforme o atributo (exatamente como está abaixo) do torcedor a ser utilizado como"
                " parâmetro na consulta:\n"
                "nome || cpf || time || idade\n"
                "Atributo escolhido: "): input("Informe o valor do atributo a ser pesquisado: ")}

            for c in mycolTorcedor.find(filtro):
                print(c)

    @staticmethod
    def exibir_torcedores():
        torcedores_cadastrados = mycolTorcedor.find()
        for c in torcedores_cadastrados:
            print(c)

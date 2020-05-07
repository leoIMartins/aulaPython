import pymongo
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbvendas"]
mycolCliente = mydb["cliente"]


def exibir_clientes():
    clientes_cadastradas = mycolCliente.find()
    for c in clientes_cadastradas:
        print(c)


class Cliente:

    def __init__(self):
        self.nome = ""
        self.telefone = ""
        self.endereco = ""
        self.cidade = ""
        self.estado = ""
        self.dada_nasc = ""

    def set_nome(self, nome):
        self.nome = nome

    def set_telefone(self, telefone):
        self.telefone = telefone

    def set_endereco(self, endereco):
        self.endereco = endereco

    def set_cidade(self, cidade):
        self.cidade = cidade

    def set_estado(self, estado):
        self.estado = estado

    def set_data_nasc(self, dada_nasc):
        self.dada_nasc = dada_nasc

    def get_nome(self):
        return self.nome

    def get_telefone(self):
        return self.telefone

    def get_endereco(self):
        return self.endereco

    def get_cidade(self):
        return self.cidade

    def get_estado(self):
        return self.estado

    def get_data_nasc(self):
        return self.dada_nasc

    def cadastrar_cliente(self):
        self.nome = input("Informe o nome do cliente: ")
        self.telefone = input("Informe o telefone do cliente: ")
        self.endereco = input("Informe o endereço do cliente: ")
        self.cidade = input("Informe a cidade do cliente: ")
        self.estado = input("Informe o estado do cliente: ")
        self.dada_nasc = input("Informe a dada de nascimento do cliente: ")
        cliente = {"nome": self.nome, "telefone": self.telefone, "endereco": self.endereco,
                   "cidade": self.cidade, "estado": self.estado, "dada_nasc": self.dada_nasc}
        mycolCliente.insert_one(cliente)
        return print("Cliente incluído com sucesso!")

    @staticmethod
    def alterar_cliente():
        exibir_clientes()
        cliente_escolhido = {"_id": ObjectId(input("Informe o ID do cliente a ser alterado: "))}
        atributo_escollhido = input("\nInforme o atributo (exatamente como está abaixo) a ser alterado no cliente:\n"
                                    "nome || telefone || endereco || cidade || estado || dada_nasc\n"
                                    "Atributo escolhido: ")

        novo_valor = {"$set": {atributo_escollhido: input("\nInforme o novo valor para o atributo: ")}}
        mycolCliente.update_one(cliente_escolhido, novo_valor)
        return print("Cliente alterado com sucesso!")

    @staticmethod
    def excluir_cliente(tudo):
        if tudo:
            mycolCliente.delete_many({})
            return print("Cliente(s) excluído(s) com sucesso!")
        else:
            exibir_clientes()
            mycolCliente.delete_one({"_id": ObjectId(input("Informe o ID do cliente a ser excluído: "))})
            return print("Cliente excluído com sucesso!")

    @staticmethod
    def consultar_cliente(tudo):
        if tudo:
            clientes_cadastrados = mycolCliente.find()

            for c in clientes_cadastrados:
                print(c)

        else:
            filtro = {input(
                "\nInforme o atributo (exatamente como está abaixo) do cliente a ser utilizado como"
                " parâmetro na consulta:\n"
                "nome || telefone || endereco || cidade || estado || dada_nasc\n"
                "Atributo escolhido: "): input("Informe o valor do atributo a ser pesquisado: ")}

            for c in mycolCliente.find(filtro):
                print(c)

    @staticmethod
    def exibir_clientes():
        clientes_cadastradas = mycolCliente.find()
        for c in clientes_cadastradas:
            print(c)

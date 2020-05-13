import pymongo
from bson import ObjectId
from datetime import date

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbvendas"]
mycolProduto = mydb["produto"]


def exibir_produtos():
    produtos_cadastradas = mycolProduto.find()
    for c in produtos_cadastradas:
        print(c)


class Produto:

    def __init__(self):
        self.nome = ""
        self.preco = ""
        self.data_entrada = ""
        self.data_saida = ""

    def set_nome(self, nome):
        self.nome = nome

    def set_preco(self, preco):
        self.preco = preco

    def set_data_entrada(self, data_entrada):
        self.data_entrada = data_entrada

    def set_data_saida(self, data_saida):
        self.data_saida = data_saida

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco

    def get_data_entrada(self):
        return self.data_entrada

    def get_data_saida(self):
        return self.data_saida

    def cadastrar_produto(self):
        self.nome = input("Informe o nome do produto: ")
        self.preco = input("Informe o preço do produto: ")
        self.data_entrada = date.today().strftime("%d/%m/%Y")
        self.data_saida = ""
        produto = {"nome": self.nome, "preco": self.preco, "data_entrada": self.data_entrada,
                   "data_saida": self.data_saida}
        mycolProduto.insert_one(produto)
        return print("Produto incluído com sucesso!")

    @staticmethod
    def alterar_produto():
        exibir_produtos()
        produto_escolhido = {"_id": ObjectId(input("Informe o ID do produto a ser alterado: "))}
        atributo_escollhido = input("\nInforme o atributo (exatamente como está abaixo) a ser alterado no produto:\n"
                                    "nome || preco\n"
                                    "Atributo escolhido: ")

        novo_valor = {"$set": {atributo_escollhido: input("\nInforme o novo valor para o atributo: ")}}
        mycolProduto.update_one(produto_escolhido, novo_valor)
        return print("Produto alterado com sucesso!")

    @staticmethod
    def excluir_produto(tudo):
        if tudo:
            mycolProduto.delete_many({})
            return print("Produto(s) excluído(s) com sucesso!")
        else:
            exibir_produtos()
            mycolProduto.delete_one({"_id": ObjectId(input("Informe o ID do produto a ser excluído: "))})
            return print("Produto excluído com sucesso!")

    @staticmethod
    def consultar_produto(tudo):
        if tudo:
            produtos_cadastrados = mycolProduto.find()

            for c in produtos_cadastrados:
                print(c)

        else:
            filtro = {input(
                "\nInforme o atributo (exatamente como está abaixo) do produto a ser utilizado como"
                " parâmetro na consulta:\n"
                "nome || preco || data_entrada || data_saida\n"
                "Atributo escolhido: "): input("Informe o valor do atributo a ser pesquisado: ")}

            for c in mycolProduto.find(filtro):
                print(c)

    @staticmethod
    def exibir_produtos(venda):
        if venda:
            produtos_cadastradas = mycolProduto.find({"data_saida": ""}, {"data_saida": 0})
        else:
            produtos_cadastradas = mycolProduto.find()
        for c in produtos_cadastradas:
            print(c)

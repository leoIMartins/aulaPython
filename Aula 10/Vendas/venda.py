import pymongo
import jsons
from bson import ObjectId
from funcionario import Funcionario
from produto import Produto
from cliente import Cliente

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbvendas"]
mycolVendas = mydb["vendas"]


class Venda:
    def __init__(self):
        self.descricao = ""
        self.produto = ""
        self.funcionario = ""
        self.cliente = ""

    def vender(self):
        self.descricao = input("Informe a descricao da venda: ")
        Produto.exibir_produtos()
        self.produto = input("Informe o ID do produto escolhido: ")
        Funcionario.exibir_funcionarios()
        self.funcionario = input("Informe o ID do funcionario escolhido: ")
        Cliente.exibir_clientes()
        self.cliente = input("Informe o ID do cliente escolhido: ")



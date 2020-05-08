import pymongo
import jsons
from bson import ObjectId
from funcionario import Funcionario
from produto import Produto
from cliente import Cliente
from datetime import date

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbvendas"]
mycolVendas = mydb["vendas"]
mycolProduto = mydb["produto"]
mycolFuncionario = mydb["funcionario"]
mycolCliente = mydb["cliente"]


class Venda:
    def __init__(self):
        self.descricao = ""
        self.produto = ""
        self.funcionario = ""
        self.cliente = ""

    @staticmethod
    def vender():
        descricao = input("Informe a descricao da venda: ")
        Produto.exibir_produtos()
        produto_escolhido = mycolProduto.find(
            {"_id": ObjectId(input("Informe o ID do produto escolhido: "))})
        Funcionario.exibir_funcionarios()
        funcionario_escolhido = mycolFuncionario.find(
            {"_id": ObjectId(input("Informe o ID do funcionario escolhido: "))})
        Cliente.exibir_clientes()
        cliente_escolhido = mycolCliente.find(
            {"_id": ObjectId(input("Informe o ID do cliente escolhido: "))})
        data = date.today().strftime("%d/%m/%Y")

        venda = {"descricao": descricao, "produto": [produto_escolhido[0]], "funcionario": [funcionario_escolhido[0]],
                 "cliente": [cliente_escolhido[0]], "data": data}

        print(produto_escolhido[0])
        print(funcionario_escolhido[0])
        print(cliente_escolhido[0])
        print(venda)

        mycolVendas.insert_one(venda)
        return print("Venda realizada com sucesso!")

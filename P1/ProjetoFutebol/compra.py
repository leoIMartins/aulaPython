import pymongo
from ingresso import Ingresso
from torcedor import Torcedor
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbfutebol"]
mycolCompra = mydb["compra"]
mycolIngresso = mydb["ingresso"]
mycolTorcedor = mydb["torcedor"]


def exibir_compras():
    compras_cadastradas = mycolCompra.find()
    for c in compras_cadastradas:
        print(c)


def validar_cadastros_realizados():
    i = 0
    lista = []
    verificacoes = ["ingressos", "torcedores"]
    ingressos_cadastrados = mycolIngresso.find()
    torcedores_cadastrados = mycolTorcedor.find()
    lista.append(ingressos_cadastrados)
    lista.append(torcedores_cadastrados)
    for list_item in lista:
        quantidade = 0
        for item in list_item:
            quantidade += 1
        print("Quantidade de ", verificacoes[i], " cadastrados: ", str(quantidade))
        if verificacoes[i] == "ingressos" and quantidade < 1:
            print("É necessário cadastrar no mínimo 1 ingresso para prosseguir!")
            return False
        elif verificacoes[i] == "torcedores" and quantidade < 1:
            print("É necessário cadastrar no mínimo 1 torcedor para prosseguir!")
            return False
        i += 1
    print("Cadastros validados com sucesso")
    return True


class Compra:

    def __init__(self):
        self.torcedor = ""
        self.ingresso = ""

    def set_cpf(self, ingresso):
        self.ingresso = ingresso

    def set_nome(self, torcedor):
        self.torcedor = torcedor

    def get_cpf(self):
        return self.ingresso

    def get_nome(self):
        return self.torcedor

    def comprar(self):
        if validar_cadastros_realizados():
            '''quantidade = 0
            self.torcedor = input("Informe o preço do compra: ")
            self.ingresso = input("Informe o ingresso da arquibancada: ")
            while quantidade < 1:
                quantidade = int(input("Informe a quantidade a ser disponibilizada: "))
                if quantidade < 1:
                    print("Informe uma quantidade maior que 0")
            for q in range(quantidade):
                compra = {"torcedor": self.torcedor, "ingresso": self.ingresso}
                mycolCompra.insert_one(compra)'''
            # PAREI AQUIIII!!!!!

            return print("Compra efetuada com sucesso!")

    @staticmethod
    def consultar_compra(tudo):
        if tudo:
            compras_cadastradas = mycolCompra.find()

            for c in compras_cadastradas:
                print(c)

        else:
            filtro = {input(
                "\nInforme o atributo (exatamente como está abaixo) da compra a ser utilizado como"
                " parâmetro na consulta:\n"
                "torcedor || ingresso\n"
                "Atributo escolhido: "): input("Informe o valor do atributo a ser pesquisado: ")}

            for c in mycolCompra.find(filtro):
                print(c)

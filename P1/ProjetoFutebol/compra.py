import pymongo
from ingresso import Ingresso
from torcedor import Torcedor
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbfutebol"]
mycolCompra = mydb["compra"]
mycolIngresso = mydb["ingresso"]
mycolTorcedor = mydb["torcedor"]

torcedor = Torcedor()
ingresso = Ingresso()

def exibir_compras():
    compras_cadastradas = mycolCompra.find()
    for c in compras_cadastradas:
        print(c)


def validar_cadastros_realizados():
    i = 0
    lista = []
    verificacoes = ["ingressos", "torcedores"]
    ingressos_cadastrados = mycolIngresso.find({"vendido": "Nao"})
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
            torcedor.exibir_torcedores()
            self.torcedor = mycolTorcedor.find({"_id": ObjectId(input("Informe o ID do torcedor: "))})
            nome_torcedor = dict(self.torcedor[0]).get("nome")
            ingresso.consultar_ingresso(True)
            id_ingresso = ObjectId(input("Informe o ID do ingresso: "))
            self.ingresso = mycolIngresso.find({"_id": id_ingresso})

            status_compra_ingresso = {"$set": {"vendido": "Sim"}}
            mycolIngresso.update_one(self.ingresso[0], status_compra_ingresso)

            compra = {"torcedor": self.torcedor[0], "ingresso": self.ingresso[0]}
            mycolCompra.insert_one(compra)
            print("Compra efetuada com sucesso!")

            ingresso_jogo = open('C:\\Python\\aulaPython\\P1\\ProjetoFutebol\\Ingresso.txt', 'w')
            jogo = dict(self.ingresso[0]).get("jogo")
            clube_a = dict(jogo).get("clube_a")
            nome_clube_a = dict(clube_a).get("nome")
            clube_b = dict(jogo).get("clube_b")
            nome_clube_b = dict(clube_b).get("nome")
            ingresso_jogo.write("Código do ingresso: %s\n" % id_ingresso)
            ingresso_jogo.write("%s X %s\n" % (nome_clube_a, nome_clube_b))
            ingresso_jogo.write("Torcedor: %s\n" % nome_torcedor)
            print("Ingresso gerado com sucesso")
            ingresso_jogo.close()

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

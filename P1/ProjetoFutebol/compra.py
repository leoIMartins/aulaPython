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


def validar_cadastros_realizados():
    i = 0
    lista = []
    verificacoes = ["ingressos", "torcedores"]
    ingressos_cadastrados = mycolIngresso.find({"vendido": "Não"})
    torcedores_cadastrados = mycolTorcedor.find()
    lista.append(ingressos_cadastrados)
    lista.append(torcedores_cadastrados)
    for list_item in lista:
        quantidade = 0
        for item in list_item:
            quantidade += 1
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
            torcedor.consultar_torcedor(True)
            self.torcedor = mycolTorcedor.find({"_id": ObjectId(input("Informe o ID do torcedor: "))})
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
            estadio = dict(jogo).get("estadio")
            nome_estadio = dict(estadio).get("nome")
            cidade_estadio = dict(estadio).get("cidade")
            descricao_jogo = dict(jogo).get("descricao")
            pais_estadio = dict(estadio).get("pais")
            torcedor_dados = dict(self.torcedor[0])
            nome_torcedor = dict(torcedor_dados).get("nome")
            cpf_torcedor = dict(torcedor_dados).get("cpf")
            idade_torcedor = dict(torcedor_dados).get("idade")
            setor_ingresso = dict(self.ingresso[0]).get("setor")
            preco_ingresso = dict(self.ingresso[0]).get("preco")

            ingresso_jogo.write("--------------------- INGRESSO ---------------------\n")
            ingresso_jogo.write("****************** DADOS DO JOGO ******************\n")
            ingresso_jogo.write("%s X %s\n" % (nome_clube_a, nome_clube_b))
            ingresso_jogo.write("Estádio: %s\n" % nome_estadio)
            ingresso_jogo.write("Cidade: %s - País: %s\n" % (cidade_estadio, pais_estadio))
            ingresso_jogo.write("Descrição do jogo: %s\n" % descricao_jogo)
            ingresso_jogo.write("**************** DADOS DO COMPRADOR ****************\n")
            ingresso_jogo.write("Torcedor: %s\n" % nome_torcedor)
            ingresso_jogo.write("CPF: %s\n" % cpf_torcedor)
            ingresso_jogo.write("Idade: %s\n" % idade_torcedor)
            ingresso_jogo.write("**************** DADOS DO INGRESSO *****************\n")
            ingresso_jogo.write("Código: %s\n" % id_ingresso)
            ingresso_jogo.write("Setor da arquibancada: %s\n" % setor_ingresso)
            ingresso_jogo.write("Preço total: R$%s" % preco_ingresso)

            print("Ingresso gerado com sucesso!")
            ingresso_jogo.close()

    @staticmethod
    def consultar_compras():
        print("\n")
        for x in mycolCompra.find():
            torcedor_dados = dict(x).get("torcedor")
            ingresso_dados = dict(x).get("ingresso")
            jogo_dados = dict(ingresso_dados).get("jogo")
            estadio_dados = dict(jogo_dados).get("estadio")
            clube_a = dict(jogo_dados).get("clube_a")
            clube_b = dict(jogo_dados).get("clube_b")

            print("ID da compra: %s" % x.get("_id"))
            print(" - Nome do torcedor: %s" % torcedor_dados.get("nome"))
            print(" - CPF do torcedor: %s" % torcedor_dados.get("cpf"))
            print(" - Código do ingresso: %s" % ingresso_dados.get("_id"))
            print(" - %s X %s" % (clube_a.get("nome"), clube_b.get("nome")))
            print(" - Estádio: %s" % estadio_dados.get("nome"))
            print("----------------------------------------------------------------------------------------------")

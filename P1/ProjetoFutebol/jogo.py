import pymongo
from bson import ObjectId
from clube import Clube
from estadio import Estadio
from torcedor import Torcedor

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbfutebol"]
mycolJogo = mydb["jogo"]
mycolClube = mydb["clube"]
mycolEstadio = mydb["estadio"]
mycolTorcedor = mydb["torcedor"]
mycolIngresso = mydb["ingresso"]

clube = Clube()
estadio = Estadio()
torcedor = Torcedor()


def validar_cadastros_realizados():
    i = 0
    lista = []
    clube_as = ["clubes", "estádios"]
    clubes_cadastrados = mycolClube.find()
    estadios_cadastrados = mycolEstadio.find()
    lista.append(clubes_cadastrados)
    lista.append(estadios_cadastrados)
    for list_item in lista:
        quantclube_b = 0
        for item in list_item:
            quantclube_b += 1
        print("Quantclube_b de ", clube_as[i], " cadastrados: ", str(quantclube_b))
        if clube_as[i] == "clubes" and quantclube_b < 2:
            print("É necessário cadastrar no mínimo 2 clubes para prosseguir!")
            return False
        elif clube_as[i] == "estádios" and quantclube_b < 1:
            print("É necessário cadastrar no mínimo 1 estádio para prosseguir!")
            return False
        i += 1
    print("Cadastros validados com sucesso")
    return True


class Jogo:

    def __init__(self):
        self.descricao = ""
        self.clube_a = ""
        self.clube_b = ""
        self.estadio = ""

    def set_descricao(self, descricao):
        self.descricao = descricao

    def set_clube_a(self, clube_a):
        self.clube_a = clube_a

    def set_clube_b(self, clube_b):
        self.clube_b = clube_b

    def set_estadio(self, estadio):
        self.estadio = estadio

    def get_descricao(self):
        return self.descricao

    def get_clube_a(self):
        return self.clube_a

    def get_clube_b(self):
        return self.clube_b

    def get_estadio(self):
        return self.estadio

    def gerar_jogo(self):
        if validar_cadastros_realizados():
            self.descricao = input("Informe a descrição da partida: ")

            clube.consultar_clube(True)
            id_clube_a = ObjectId(input("Informe o ID do clube A: "))
            self.clube_a = mycolClube.find({"_id": id_clube_a})
            id_clube_b = id_clube_a
            while id_clube_b == id_clube_a:
                clube.consultar_clube(True)
                id_clube_b = ObjectId(input("Informe o ID do clube B: "))
                self.clube_b = mycolClube.find({"_id": id_clube_b})
                if id_clube_b == id_clube_a:
                    print("O ID dos clubes A e B devem ser diferentes!")

            estadio.consultar_estadio(True)
            self.estadio = mycolEstadio.find(
                {"_id": ObjectId(input("Informe o ID do estádio: "))})
            jogo = {"descricao": self.descricao, "clube_a": self.clube_a[0],
                    "clube_b": self.clube_b[0], "estadio": self.estadio[0]}
            mycolJogo.insert_one(jogo)
            return print("Jogo gerado com sucesso!")

    @staticmethod
    def exibir_jogos():
        print("\n")
        for x in mycolJogo.find():
            clube_a = dict(x).get("clube_a")
            clube_b = dict(x).get("clube_b")
            estadio_dados = dict(x).get("estadio")
            print("ID: %s" % x.get("_id"))
            print(" - Descrição do jogo: %s" % x.get("descricao"))
            print(" - %s X %s" % (clube_a.get("nome"), clube_b.get("nome")))
            print(" - Estádio: %s" % estadio_dados.get("nome"))
            print("----------------------------------------------------------------------------------------------")

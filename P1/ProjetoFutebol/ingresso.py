import pymongo
from bson import ObjectId
from jogo import Jogo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbfutebol"]
mycolIngresso = mydb["ingresso"]
mycolJogo = mydb["jogo"]

jogo = Jogo()


def exibir_ingressos():
    print("\n")
    for x in mycolIngresso.find():
        jogo_dados = dict(x).get("jogo")
        clube_a = dict(jogo_dados).get("clube_a")
        clube_b = dict(jogo_dados).get("clube_b")
        estadio = dict(jogo_dados).get("estadio")
        print("ID: %s" % x.get("_id"))
        print(" - Preço: R$%s" % x.get("preco"))
        print(" - Setor: %s" % x.get("setor"))
        print(" - Descrição do jogo: %s" % jogo_dados.get("descricao"))
        print(" - %s X %s" % (clube_a.get("nome"), clube_b.get("nome")))
        print(" - Estádio: %s" % estadio.get("nome"))
        print(" - Disponível: %s" % x.get("vendido"))
        print("----------------------------------------------------------------------------------------------")


def validar_cadastros_realizados():
    quantidade_jogos = 0
    jogos_cadastrados = mycolJogo.find()
    for j in jogos_cadastrados:
        quantidade_jogos += 1
    print("Jogos cadastrados: ", str(quantidade_jogos))
    if quantidade_jogos < 1:
        print("É necessário cadastrar no mínimo 1 jogo para prosseguir!")
        return False
    print("Cadastros validados com sucesso")
    return True


class Ingresso:

    def __init__(self):
        self.preco = ""
        self.setor = ""
        self.jogo = ""

    def set_cpf(self, setor):
        self.setor = setor

    def set_nome(self, preco):
        self.preco = preco

    def set_jogo(self, jogo):
        self.jogo = jogo

    def get_cpf(self):
        return self.setor
    
    def get_nome(self):
        return self.preco

    def get_jogo(self):
        return self.jogo

    def cadastrar_ingresso(self):
        if validar_cadastros_realizados():
            quantidade = 0
            self.preco = input("Informe o preço do ingresso: ")
            self.setor = input("Informe o setor da arquibancada: ")
            Jogo.exibir_jogos()
            self.jogo = mycolJogo.find(
                {"_id": ObjectId(input("Informe o ID do jogo: "))})
            while quantidade < 1:
                quantidade = int(input("Informe a quantidade a ser disponibilizada: "))
                if quantidade < 1:
                    print("Informe uma quantidade maior que 0")
            for q in range(quantidade):
                ingresso = {"preco": self.preco, "setor": self.setor, "jogo": self.jogo[0], "vendido": "Nao"}
                mycolIngresso.insert_one(ingresso)

            return print("Ingresso(s) incluído(s) com sucesso!")

    @staticmethod
    def excluir_ingresso(tudo):
        mycolIngresso.delete_many({})
        return print("Ingresso(s) excluído(s) com sucesso!")

    @staticmethod
    def consultar_ingresso(disponivel):
        print("\n")
        if disponivel:
            ingressos_cadastrados = mycolIngresso.find({"vendido": "Nao"}, {"vendido": 0})
        else:
            ingressos_cadastrados = mycolIngresso.find()
        for x in ingressos_cadastrados:
            jogo_dados = dict(x).get("jogo")
            clube_a = dict(jogo_dados).get("clube_a")
            clube_b = dict(jogo_dados).get("clube_b")
            estadio = dict(jogo_dados).get("estadio")
            print("ID: %s" % x.get("_id"))
            print(" - Preço: R$%s" % x.get("preco"))
            print(" - Setor: %s" % x.get("setor"))
            print(" - Descrição do jogo: %s" % jogo_dados.get("descricao"))
            print(" - %s X %s" % (clube_a.get("nome"), clube_b.get("nome")))
            print(" - Estádio: %s" % estadio.get("nome"))
            if not disponivel:
                print(" - Disponível: %s" % x.get("vendido"))
            print("----------------------------------------------------------------------------------------------")

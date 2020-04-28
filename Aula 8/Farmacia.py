import pymongo
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbatividade"]
mycolFarmacia = mydb["farmacia"]


def exibir_farmacias():
    farmacias_cadastradas = mycolFarmacia.find()
    for f in farmacias_cadastradas:
        print(f)


class Farmacia:

    def __init__(self):
        self.descricao = ""
        self.qtd_funcionarios = ""
        self.qtd_medicamentos = ""
        self.endereco = ""
        self.telefone = ""
        self.cidade = ""
        self.estado = ""

    def set_descricao(self, descricao):
        self.descricao = descricao

    def set_qtd_funcionarios(self, qtd_funcionarios):
        self.qtd_funcionarios = qtd_funcionarios

    def set_qtd_medicamentos(self, qtd_medicamentos):
        self.qtd_medicamentos = qtd_medicamentos

    def set_endereco(self, endereco):
        self.endereco = endereco

    def set_telefone(self, telefone):
        self.telefone = telefone

    def set_cidade(self, cidade):
        self.cidade = cidade

    def set_estado(self, estado):
        self.estado = estado

    def get_descricao(self):
        return self.descricao

    def get_qtd_funcionarios(self):
        return self.qtd_funcionarios

    def get_qtd_medicamentos(self):
        return self.qtd_medicamentos

    def get_endereco(self):
        return self.endereco

    def get_telefone(self):
        return self.telefone

    def get_cidade(self):
        return self.cidade

    def get_estado(self):
        return self.estado

    def cadastrar_farmacia(self):
        self.descricao = input("Informe a descrição da farmácia: ")
        self.qtd_funcionarios = input("Informe a quantidade de funcionários da farmácia: ")
        self.qtd_medicamentos = input("Informe a quantidade de medicamentos da farmácia: ")
        self.endereco = input("Informe o endereço da farmácia: ")
        self.telefone = input("Informe o telefone da farmácia: ")
        self.cidade = input("Informe a cidade da farmácia: ")
        self.estado = input("Informe o estado da farmácia: ")
        farmacia = {"descricao": self.descricao, "qtd_funcionarios": self.qtd_funcionarios,
                    "qtd_medicamentos": self.qtd_medicamentos, "endereco": self.endereco,
                    "telefone": self.telefone, "cidade": self.cidade, "estado": self.estado}
        mycolFarmacia.insert_one(farmacia)
        return print("Farmácia incluída com sucesso!")

    @staticmethod
    def alterar_farmacia():
        exibir_farmacias()
        farmacia_escolhida = {"_id": ObjectId(input("Informe o ID da farmácia a ser alterada: "))}
        atributo_escollhido = input("\nInforme o atributo (exatamente como está abaixo) a ser alterado no livro:\n"
                                    "descricao || qtd_funcionarios || qtd_medicamentos || endereco || telefone || "
                                    "cidade || estado\n"
                                    "Atributo escolhido: ")

        novo_valor = {"$set": {atributo_escollhido: input("\nInforme o novo valor para o atributo: ")}}
        mycolFarmacia.update_one(farmacia_escolhida, novo_valor)

    @staticmethod
    def excluir_farmacia(tudo):
        if tudo:
            mycolFarmacia.delete_many({})
        else:
            exibir_farmacias()
            mycolFarmacia.delete_one({"_id": ObjectId(input("Informe o ID da farmácia a ser excluída: "))})

    @staticmethod
    def consultar_farmacia(tudo):
        if tudo:
            farmacias_cadastradas = mycolFarmacia.find()

            for f in farmacias_cadastradas:
                print(f)

        else:
            filtro = {input(
                "\nInforme o atributo (exatamente como está abaixo) de pessoa a ser utilizado como"
                " parâmetro na consulta:\n"
                "descricao || qtd_funcionarios || qtd_medicamentos || endereco || telefone || cidade || estado\n"
                "Atributo escolhido: "): input("Informe o valor do atributo a ser pesquisado: ")}

            for f in mycolFarmacia.find(filtro):
                print(f)

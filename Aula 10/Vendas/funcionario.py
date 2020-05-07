import pymongo
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbvendas"]
mycolFuncionario = mydb["funcionario"]


def exibir_funcionarios():
    funcionarios_cadastradas = mycolFuncionario.find()
    for c in funcionarios_cadastradas:
        print(c)


class Funcionario:

    def __init__(self):
        self.nome = ""
        self.telefone = ""
        self.endereco = ""
        self.cidade = ""
        self.estado = ""
        self.dada_nasc = ""
        self.salario = ""

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

    def set_salario(self, salario):
        self.salario = salario

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

    def get_salario(self):
        return self.salario

    def cadastrar_funcionario(self):
        self.nome = input("Informe o nome do funcionario: ")
        self.telefone = input("Informe o telefone do funcionario: ")
        self.endereco = input("Informe o endereço do funcionario: ")
        self.cidade = input("Informe a cidade do funcionario: ")
        self.estado = input("Informe o estado do funcionario: ")
        self.dada_nasc = input("Informe a dada de nascimento do funcionario: ")
        self.salario = input("Informe o salario do funcionario: ")
        funcionario = {"nome": self.nome, "telefone": self.telefone, "endereco": self.endereco,
                       "cidade": self.cidade, "estado": self.estado, "dada_nasc": self.dada_nasc,
                       "salario": self.salario}
        mycolFuncionario.insert_one(funcionario)
        return print("Funcionario incluído com sucesso!")

    @staticmethod
    def alterar_funcionario():
        exibir_funcionarios()
        funcionario_escolhido = {"_id": ObjectId(input("Informe o ID do funcionario a ser alterado: "))}
        atributo_escollhido = input("\nInforme o atributo (exatamente como está abaixo) a ser alterado no funcionario:"
                                    "\nnome || telefone || endereco || cidade || estado || dada_nasc || salario\n"
                                    "Atributo escolhido: ")

        novo_valor = {"$set": {atributo_escollhido: input("\nInforme o novo valor para o atributo: ")}}
        mycolFuncionario.update_one(funcionario_escolhido, novo_valor)
        return print("Funcionario alterado com sucesso!")

    @staticmethod
    def excluir_funcionario(tudo):
        if tudo:
            mycolFuncionario.delete_many({})
            return print("Funcionario(s) excluído(s) com sucesso!")
        else:
            exibir_funcionarios()
            mycolFuncionario.delete_one({"_id": ObjectId(input("Informe o ID do funcionario a ser excluído: "))})
            return print("Funcionario excluído com sucesso!")

    @staticmethod
    def consultar_funcionario(tudo):
        if tudo:
            funcionarios_cadastrados = mycolFuncionario.find()

            for c in funcionarios_cadastrados:
                print(c)

        else:
            filtro = {input(
                "\nInforme o atributo (exatamente como está abaixo) do funcionario a ser utilizado como"
                " parâmetro na consulta:\n"
                "nome || telefone || endereco || cidade || estado || dada_nasc || salario\n"
                "Atributo escolhido: "): input("Informe o valor do atributo a ser pesquisado: ")}

            for c in mycolFuncionario.find(filtro):
                print(c)

    @staticmethod
    def exibir_funcionarios():
        funcionarios_cadastradas = mycolFuncionario.find()
        for c in funcionarios_cadastradas:
            print(c)

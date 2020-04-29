import pymongo
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbatividade"]
mycolMedicamento = mydb["medicamento"]


def exibir_medicamentos():
    medicamentos_cadastradas = mycolMedicamento.find()
    for m in medicamentos_cadastradas:
        print(m)


class Medicamento:

    def __init__(self):
        self.descricao = ""

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_descricao(self):
        return self.descricao

    def cadastrar_medicamento(self):
        self.descricao = input("Informe a descrição do medicamento: ")
        
        medicamento = {"descricao": self.descricao}
        mycolMedicamento.insert_one(medicamento)
        return print("Medicamento incluído com sucesso!")

    @staticmethod
    def alterar_medicamento():
        exibir_medicamentos()
        medicamento_escolhido = {"_id": ObjectId(input("Informe o ID do medicamento a ser alterado: "))}

        novo_valor = {"$set": {"descricao": input("\nInforme uma nova descrição: ")}}
        mycolMedicamento.update_one(medicamento_escolhido, novo_valor)
        return print("Medicamento alterado com sucesso!")

    @staticmethod
    def excluir_medicamento(tudo):
        if tudo:
            mycolMedicamento.delete_many({})
            return print("Medicamento(s) excluído(s) com sucesso!")
        else:
            exibir_medicamentos()
            mycolMedicamento.delete_one({"_id": ObjectId(input("Informe o ID do medicamento a ser excluído: "))})
            return print("Medicamento excluído com sucesso!")

    @staticmethod
    def consultar_medicamento(tudo):
        if tudo:
            medicamentos_cadastrados = mycolMedicamento.find()

            for m in medicamentos_cadastrados:
                print(m)

        else:
            filtro = {"descricao": input("Informe a descrição do medicamento a ser pesquisado: ")}

            for f in mycolMedicamento.find(filtro):
                print(f)

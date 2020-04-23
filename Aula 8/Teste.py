import pymongo
# noinspection PyUnresolvedReferences
from Farmacia import Farmacia

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbatividade"]
mycolFarmacia = mydb["farmacia"]

# farmacia = Farmacia("descrição teste", "8", "9579", "Rua Antonio Braga, 384", "(11)3324-7538", "São Paulo", "SP")


while True:
    option = input("\n1 - Cadastrar farmácia\n"
                   "0 - Sair\n"
                   "Opção escolhida: ")

    if option == "1":
        descricao = input("Informe a descrição da farmácia: ")
        qtd_funcionarios = input("Informe a quantidade de funcionários da farmácia: ")
        qtd_medicamentos = input("Informe a quantidade de medicamentos da farmácia: ")
        endereco = input("Informe o endereço da farmácia: ")
        telefone = input("Informe o telefone da farmácia: ")
        cidade = input("Informe a cidade da farmácia: ")
        estado = input("Informe o estado da farmácia: ")

        farmacia = Farmacia()
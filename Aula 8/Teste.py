import pymongo
# noinspection PyUnresolvedReferences
from Farmacia import Farmacia

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbatividade"]
mycolFarmacia = mydb["farmacia"]

farmacia = Farmacia()

while True:
    option = input("\n1 - Manter Farmácia\n"
                   "2 - Manter Medicamento\n"
                   "3 - Manter Cliente\n"
                   "0 - Sair\n"
                   "Opção escolhida: ")

    if option == "1":
        option = input("\n1 - Cadastrar Farmácia\n"
                       "2 - Alterar Farmácia\n"
                       "3 - Excluir Farmácia\n"
                       "4 - Consultar Farmácia\n"
                       "0 - Sair\n"
                       "Opção escolhida: ")

        if option == "1":
            farmacia.cadastrar_farmacia()
        elif option == "2":
            farmacia.alterar_farmacia()
        elif option == "3":
            opcao = input("\n1 - Excluir farmácia específica\n"
                          "2 - Excluir todas as farmácias\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                farmacia.excluir_farmacia(False)
            elif opcao == "2":
                opcao = input("Tem certeza que deseja excluir todas as farmácias? (s/n): ")
                if opcao == "s":
                    farmacia.excluir_farmacia(True)
                else:
                    continue

        elif option == "4":
            opcao = input("\n1 - Consultar todas as farmácias\n"
                          "2 - Consulta personalizada\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                farmacia.consultar_farmacia(True)
            elif opcao == "2":
                farmacia.consultar_farmacia(False)
        else:
            continue

    '''if option == "2":
        option = input("\n1 - Cadastrar Medicamento\n"
                       "2 - Alterar Medicamento\n"
                       "3 - Excluir Medicamento\n"
                       "4 - Consultar Medicamento\n"
                       "0 - Sair\n"
                       "Opção escolhida: ")

        if option == "1":
            medicamento.cadastrar_medicamento()
        elif option == "2":
            medicamento.alterar_medicamento()
        elif option == "3":
            medicamento.excluir_medicamento()
        elif option == "4":
            medicamento.consultar_medicamento()
        else:
            continue

    if option == "3":
        option = input("\n1 - Cadastrar Cliente\n"
                       "2 - Alterar Cliente\n"
                       "3 - Excluir Cliente\n"
                       "4 - Consultar Cliente\n"
                       "0 - Sair\n"
                       "Opção escolhida: ")

        if option == "1":
            cliente.cadastrar_cliente()
        elif option == "2":
            cliente.alterar_cliente()
        elif option == "3":
            cliente.excluir_cliente()
        elif option == "4":
            cliente.consultar_cliente()
        else:
            continue'''

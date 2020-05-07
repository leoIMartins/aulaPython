import pymongo
from farmacia import Farmacia
from medicamento import Medicamento
from cliente import Cliente

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbatividade"]
mycolFarmacia = mydb["farmacia"]

farmacia = Farmacia()
medicamento = Medicamento()
cliente = Cliente()


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

    elif option == "2":
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
            opcao = input("\n1 - Excluir medicamento específico\n"
                          "2 - Excluir todos os medicamentos\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                medicamento.excluir_medicamento(False)
            elif opcao == "2":
                opcao = input("Tem certeza que deseja excluir todos os medicamentos? (s/n): ")
                if opcao == "s":
                    medicamento.excluir_medicamento(True)
                else:
                    continue

        elif option == "4":
            opcao = input("\n1 - Consultar todos os medicamentos\n"
                          "2 - Consulta personalizada\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                medicamento.consultar_medicamento(True)
            elif opcao == "2":
                medicamento.consultar_medicamento(False)
        else:
            continue

    elif option == "3":
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
            opcao = input("\n1 - Excluir cliente específico\n"
                          "2 - Excluir todos os clientes\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                cliente.excluir_cliente(False)
            elif opcao == "2":
                opcao = input("Tem certeza que deseja excluir todos os clientes? (s/n): ")
                if opcao == "s":
                    cliente.excluir_cliente(True)
                else:
                    continue

        elif option == "4":
            opcao = input("\n1 - Consultar todos os clientes\n"
                          "2 - Consulta personalizada\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                cliente.consultar_cliente(True)
            elif opcao == "2":
                cliente.consultar_cliente(False)
        else:
            continue

    elif option == "0":
        break

    else:
        print("Informe uma opção válida!")

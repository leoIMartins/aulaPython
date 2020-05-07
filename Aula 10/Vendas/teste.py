import pymongo
from funcionario import Funcionario
from produto import Produto
from cliente import Cliente

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbvendas"]

funcionario = Funcionario()
produto = Produto()
cliente = Cliente()


while True:
    option = input("\n1 - Manter Funcionário\n"
                   "2 - Manter Produto\n"
                   "3 - Manter Cliente\n"
                   "0 - Sair\n"
                   "Opção escolhida: ")

    if option == "1":
        option = input("\n1 - Cadastrar Funcionário\n"
                       "2 - Alterar Funcionário\n"
                       "3 - Excluir Funcionário\n"
                       "4 - Consultar Funcionário\n"
                       "0 - Sair\n"
                       "Opção escolhida: ")

        if option == "1":
            funcionario.cadastrar_funcionario()
        elif option == "2":
            funcionario.alterar_funcionario()
        elif option == "3":
            opcao = input("\n1 - Excluir funcionário específica\n"
                          "2 - Excluir todas as funcionários\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                funcionario.excluir_funcionario(False)
            elif opcao == "2":
                opcao = input("Tem certeza que deseja excluir todas as funcionários? (s/n): ")
                if opcao == "s":
                    funcionario.excluir_funcionario(True)
                else:
                    continue

        elif option == "4":
            opcao = input("\n1 - Consultar todas as funcionários\n"
                          "2 - Consulta personalizada\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                funcionario.consultar_funcionario(True)
            elif opcao == "2":
                funcionario.consultar_funcionario(False)
        else:
            continue

    elif option == "2":
        option = input("\n1 - Cadastrar Produto\n"
                       "2 - Alterar Produto\n"
                       "3 - Excluir Produto\n"
                       "4 - Consultar Produto\n"
                       "0 - Sair\n"
                       "Opção escolhida: ")

        if option == "1":
            produto.cadastrar_produto()
        elif option == "2":
            produto.alterar_produto()
        elif option == "3":
            opcao = input("\n1 - Excluir produto específico\n"
                          "2 - Excluir todos os produtos\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                produto.excluir_produto(False)
            elif opcao == "2":
                opcao = input("Tem certeza que deseja excluir todos os produtos? (s/n): ")
                if opcao == "s":
                    produto.excluir_produto(True)
                else:
                    continue

        elif option == "4":
            opcao = input("\n1 - Consultar todos os produtos\n"
                          "2 - Consulta personalizada\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                produto.consultar_produto(True)
            elif opcao == "2":
                produto.consultar_produto(False)
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

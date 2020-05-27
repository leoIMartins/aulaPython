import pymongo
from clube import Clube
from estadio import Estadio
from jogo import Jogo
from ingresso import Ingresso
from torcedor import Torcedor
from compra import Compra

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbfutebol"]

clube = Clube()
estadio = Estadio()
jogo = Jogo()
ingresso = Ingresso()
torcedor = Torcedor()
compra = Compra()


while True:
    option = input("\n1 - Clube\n"
                   "2 - Estádio\n"
                   "3 - Torcedor\n"
                   "4 - Ingresso\n"
                   "5 - Jogo\n"
                   "6 - Compra\n"
                   "0 - Sair\n"
                   "Opção escolhida: ")

    if option == "1":
        option = input("\n1 - Cadastrar Clube\n"
                       "2 - Alterar Clube\n"
                       "3 - Excluir Clube\n"
                       "4 - Consultar Clube\n"
                       "0 - Sair\n"
                       "Opção escolhida: ")

        if option == "1":
            clube.cadastrar_clube()
        elif option == "2":
            clube.alterar_clube()
        elif option == "3":
            opcao = input("\n1 - Excluir clube específico\n"
                          "2 - Excluir todos os clubes\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                clube.excluir_clube(False)
            elif opcao == "2":
                opcao = input("Tem certeza que deseja excluir todos os clubes? (s/n): ")
                if opcao == "s":
                    clube.excluir_clube(True)
                else:
                    continue

        elif option == "4":
            opcao = input("\n1 - Consultar todos os clubles\n"
                          "2 - Consulta personalizada\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                clube.consultar_clube(True)
            elif opcao == "2":
                clube.consultar_clube(False)
        else:
            continue

    elif option == "2":
        option = input("\n1 - Cadastrar Estádio\n"
                       "2 - Alterar Estádio\n"
                       "3 - Excluir Estádio\n"
                       "4 - Consultar Estádio\n"
                       "0 - Sair\n"
                       "Opção escolhida: ")

        if option == "1":
            estadio.cadastrar_estadio()
        elif option == "2":
            estadio.alterar_estadio()
        elif option == "3":
            opcao = input("\n1 - Excluir estádio específico\n"
                          "2 - Excluir todos os estádios\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                estadio.excluir_estadio(False)
            elif opcao == "2":
                opcao = input("Tem certeza que deseja excluir todos os estádios? (s/n): ")
                if opcao == "s":
                    estadio.excluir_estadio(True)
                else:
                    continue

        elif option == "4":
            opcao = input("\n1 - Consultar todos os estádios\n"
                          "2 - Consulta personalizada\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                estadio.consultar_estadio(True)
            elif opcao == "2":
                estadio.consultar_estadio(False)
        else:
            continue

    elif option == "3":
        option = input("\n1 - Cadastrar Torcedor\n"
                       "2 - Alterar Torcedor\n"
                       "3 - Excluir Torcedor\n"
                       "4 - Consultar Torcedor\n"
                       "0 - Sair\n"
                       "Opção escolhida: ")

        if option == "1":
            torcedor.cadastrar_torcedor()
        elif option == "2":
            torcedor.alterar_torcedor()
        elif option == "3":
            opcao = input("\n1 - Excluir torcedor específico\n"
                          "2 - Excluir todos os torcedores\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                torcedor.excluir_torcedor(False)
            elif opcao == "2":
                opcao = input("Tem certeza que deseja excluir todos os torcedores? (s/n): ")
                if opcao == "s":
                    torcedor.excluir_torcedor(True)
                else:
                    continue

        elif option == "4":
            opcao = input("\n1 - Consultar todos os torcedores\n"
                          "2 - Consulta personalizada\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                torcedor.consultar_torcedor(True)
            elif opcao == "2":
                torcedor.consultar_torcedor(False)
        else:
            continue

    elif option == "4":
        option = input("\n1 - Cadastrar Ingresso\n"
                       "2 - Excluir Todos os Ingressos\n"
                       "3 - Consultar Todos os Ingressos\n"
                       "0 - Sair\n"
                       "Opção escolhida: ")

        if option == "1":
            ingresso.cadastrar_ingresso()
        elif option == "2":
            opcao = input("Tem certeza que deseja excluir todos os ingressos? (s/n): ")
            if opcao == "s":
                ingresso.excluir_ingressos()
            else:
                continue

        elif option == "3":
            ingresso.consultar_ingresso(False)

    elif option == "5":
        option = input("\n1 - Cadastrar Jogo\n"
                       "2 - Consultar Todos os Jogos\n"
                       "0 - Sair\n"
                       "Opção escolhida: ")
        if option == "1":
            jogo.gerar_jogo()
        elif option == "2":
            jogo.exibir_jogos()

    elif option == "6":
        option = input("\n1 - Comprar Ingresso\n"
                       "2 - Consultar Todas as Compras\n"
                       "0 - Sair\n"
                       "Opção escolhida: ")

        if option == "1":
            compra.comprar()
        elif option == "2":
            compra.consultar_compras()

    elif option == "0":
        break

    else:
        print("Informe uma opção válida!")

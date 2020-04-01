filmes = []
avaliacoes = []
associacoes = []

while True:
    opcao = input("\n1 - Inserir Filme  || "
                  "2 - Listar Filmes || "
                  "3 - Excluir Filme || "
                  "4 - Inserir Avaliação || "
                  "5 - Listar Avaliações\n"
                  "6 - Associar Avaliação ao Filme || "
                  "7 - Imprimir Relatório (Filme/Avaliação) || "
                  "8 - Sair\n"
                  "Opção escolhida: ")

    if opcao == "1":
        filme = input("Informe o nome do filme: ")
        filmes.append(filme)
        print("O filme %s foi adicionado à lista!" % filme)

    elif opcao == "2":
        print("Filmes inseridos:")
        i = 1
        for f in filmes:
            print("\t\t%d - %s" % (i, f))
            i += 1

    elif opcao == "3":
        excluir = input("Informe o nome do filme a ser excluído: ")
        if filmes.__contains__(excluir):
            filmes.remove(excluir)
            print("O filme %s foi removido da lista!" % excluir)
        else:
            print("O filme %s não existe na lista!" % excluir)

    elif opcao == "4":
        avaliacao = input("Descreva a avaliação: ")
        avaliacoes.append(avaliacao)
        print("A avaliação foi adicionada com sucesso!")

    elif opcao == "5":
        print("Avaliações inseridas:")
        i = 1
        for a in avaliacoes:
            print("\t\t%d - %s" % (i, a))
            i += 1

    elif opcao == "6":
        n = 0
        i = 1
        for f in filmes:
            print("\t\t%d - %s" % (i, f))
            i += 1
        opcaoFilme = int(input("Informe o número do filme: ")) - 1
        associacoes.append(filmes[opcaoFilme])
        i = 1
        for a in avaliacoes:
            print("\t\t%d - %s" % (i, a))
            i += 1
        opcaoAvaliacao = int(input("Informe o número da avaliação a ser associada ao filme: ")) - 1
        associacoes.append(avaliacoes[opcaoAvaliacao])
        print("A avaliação %s foi associada ao filme %s!" % (avaliacoes[opcaoAvaliacao], filmes[opcaoFilme]))

    elif opcao == "7":
        rel = open('C:\\Python\\Aula 4\\Aplicação com menu\\Relatorio.txt', 'w')
        rel.write("FILME       //       AVALIAÇÃO\n\n")
        i = 0
        for j in associacoes:
            if i % 2 == 0:
                rel.write("%s // " % (associacoes[i]))
            else:
                rel.write("%s\n" % (associacoes[i]))
            i += 1

        print("Relatório impresso com sucesso!")
        rel.close()

    elif opcao == "8":
        break

    else:
        print("\nOpção inválida! Informe uma das seguintes opções:")

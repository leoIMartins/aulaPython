import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabaseatividade"]
mycolPessoa = mydb["pessoa"]
mycolLivros = mydb["livros"]

listaPessoas = [
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
    {"nome": "Leonardo", "telefone": "16 91234 5678", "cidade": "Araraquara", "endereco": "Rua teste teste",
     "email": "leonardo_ignacio2010@hotmail.com", "nome_pai": "Álvaro Martins", "nome_mae": "Monica Martins"},
    {"nome": "Rubia", "telefone": "16 11111 2222", "cidade": "Curitiba", "endereco": "Rua teste 222",
     "email": "rubia@teste.com", "nome_pai": "Jose Silva", "nome_mae": "Maria Silva"},
]
listaLivros = [
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
    {"titulo": "senhor dos aneis", "descricao": "descricao teste", "anolancamento": "2019", "autor": "2222 autor",
     "editora": "bbbeditorabbb", "qtdpaginas": "548", "categoria": "aventura"},
    {"titulo": "narnia", "descricao": "DESCRICAO DESCRICAO", "anolancamento": "1998", "autor": "autor 1111",
     "editora": "aaaeditoraaaa", "qtdpaginas": "856", "categoria": "ficcao"},
]


def exibir_registros(pessoa):
    if pessoa:
        pessoas_cadastradas = mycolPessoa.find({}, {"_id": 0}).sort("nome", 1)
        i = 1
        for p in pessoas_cadastradas:
            print(str(i) + " - " + str(p))
            i += 1
    else:
        livros_cadastrados = mycolLivros.find({}, {"_id": 0}).sort("titulo", 1)
        i = 1
        for l in livros_cadastrados:
            print(str(i) + " - " + str(l))
            i += 1


def inserir_pessoa():
    pessoa = {"nome": input("Informe o nome da pessoa: "),
              "telefone": input("Informe o telefone da pessoa: "),
              "cidade": input("Informe a cidade da pessoa: "),
              "endereco": input("Informe o endereco da pessoa: "),
              "email": input("Informe o email da pessoa: "),
              "nome_pai": input("Informe o nome do pai da pessoa: "),
              "nome_mae": input("Informe o nome da mãe da pessoa: ")}
    mycolPessoa.insert_one(pessoa)


def inserir_livro():
    livro = {"titulo": input("Informe o título do livro: "),
             "descricao": input("Informe a descrição do livro: "),
             "anolancamento": input("Informe o ano de lançamento do livro: "),
             "autor": input("Informe o autor do livro: "),
             "editora": input("Informe a editora do livro: "),
             "qtdpaginas": input("Informe a quantidade de páginas do livro: "),
             "categoria": input("Informe a categoria do livro: ")}
    mycolLivros.insert_one(livro)


def inserir_massa_teste():
    mycolPessoa.insert_many(listaPessoas)
    mycolLivros.insert_many(listaLivros)


def alterar_pessoa():
    exibir_registros(True)
    pessoa_escolhida = {"telefone": input("\nInforme o telefone da pessoa que quer alterar: ")}
    atributo_escollhido = input("\nInforme o atributo (exatamente como está abaixo) a ser alterado na pessoa:\n"
                                "nome || telefone || cidade || endereço || email || nome_pai || nome_mae\n"
                                "Atributo escolhido: ")

    novo_valor = {"$set": {atributo_escollhido: input("\nInforme o novo valor para o atributo: ")}}
    mycolPessoa.update_one(pessoa_escolhida, novo_valor)


def alterar_livro():
    exibir_registros(False)

    livro_escolhido = {"titulo": input("\nInforme o título do livro que quer alterar: ")}
    atributo_escollhido = input("\nInforme o atributo (exatamente como está abaixo) a ser alterado no livro:\n"
                                "titulo || descricao || anolancamento || autor || editora || qtdpaginas || categoria\n"
                                "Atributo escolhido: ")

    novo_valor = {"$set": {atributo_escollhido: input("\nInforme o novo valor para o atributo: ")}}
    mycolLivros.update_one(livro_escolhido, novo_valor)


def excluir(pessoa, tudo):
    if pessoa:
        if tudo:
            x = mycolPessoa.delete_many({})
        else:
            exibir_registros(True)

            pessoa_escolhida = {"nome": input("\nInforme o nome da pessoa que quer excluir: ")}
            mycolPessoa.delete_one(pessoa_escolhida)
    else:
        if tudo:
            x = mycolLivros.delete_many({})
        else:
            livros_cadastrados = mycolLivros.find({}, {"_id": 0}).sort("titulo", 1)
            i = 1
            for l in livros_cadastrados:
                print(str(i) + " - " + str(l))
                i += 1

            livro_escolhido = {"titulo": input("\nInforme o título do livro que quer excluir: ")}
            mycolLivros.delete_one(livro_escolhido)


while True:
    option = input("\n1 - Inserir registro\n"
                   "2 - Alterar registro\n"
                   "3 - Excluir registro\n"
                   "4 - Consultar registro\n"
                   "0 - Sair\n"
                   "Opção escolhida: ")

    if option == "1":
        table = input("\n1 - Inserir pessoa\n"
                      "2 - Inserir livro\n"
                      "3 - Inserir registros de teste\n"
                      "Informe qualquer outro caractere para voltar ao menu\n"
                      "Opção escolhida: ")

        if table == "1":
            inserir_pessoa()
        elif table == "2":
            inserir_livro()
        elif table == "3":
            inserir_massa_teste()
        else:
            continue

    elif option == "2":
        table_update = input("\n1 - Alterar pessoa\n"
                             "2 - Alterar livro\n"
                             "Informe qualquer outro caractere para voltar ao menu\n"
                             "Opção escolhida: ")

        if table_update == "1":
            alterar_pessoa()
        elif table_update == "2":
            alterar_livro()
        else:
            continue

    elif option == "3":
        table_delete = input("\n1 - Excluir pessoa\n"
                             "2 - Excluir livro\n"
                             "Informe qualquer outro caractere para voltar ao menu\n"
                             "Opção escolhida: ")

        if table_delete == "1":
            opcao = input("\n1 - Excluir pessoa específica\n"
                          "2 - Excluir todas as pessoas\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")

            if opcao == "1":
                excluir(True, False)
            elif opcao == "2":
                opcao = input("Tem certeza que deseja excluir todas as pessoas? (s/n): ")
                if opcao == "s":
                    excluir(True, True)
                else:
                    continue
            else:
                continue

        elif table_delete == "2":
            opcao = input("\n1 - Excluir livro específico\n"
                          "2 - Excluir todos os livros\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                excluir(False, False)
            elif opcao == "2":
                opcao = input("Tem certeza que deseja excluir todos os livros? (s/n): ")
                if opcao == "s":
                    excluir(False, True)
                else:
                    continue
        else:
            continue

    elif option == "4":
        pass

    elif option == "0":
        break

    else:
        print("Informe uma opção válida")

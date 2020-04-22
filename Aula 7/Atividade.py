import pymongo
import time
from bson import ObjectId

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
        pessoas_cadastradas = mycolPessoa.find().sort("nome", 1)
        for p in pessoas_cadastradas:
            print(p)
    else:
        livros_cadastrados = mycolLivros.find().sort("titulo", 1)
        for c in livros_cadastrados:
            print(c)


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
    pessoa_escolhida = {"_id": ObjectId(input("Informe o ID da pessoa a ser alterada: "))}
    atributo_escollhido = input("\nInforme o atributo (exatamente como está abaixo) a ser alterado na pessoa:\n"
                                "nome || telefone || cidade || endereço || email || nome_pai || nome_mae\n"
                                "Atributo escolhido: ")

    novo_valor = {"$set": {atributo_escollhido: input("\nInforme o novo valor para o atributo: ")}}
    mycolPessoa.update_one(pessoa_escolhida, novo_valor)


def alterar_livro():
    exibir_registros(False)

    livro_escolhido = {"_id": ObjectId(input("Informe o ID do livro a ser alterado: "))}
    atributo_escollhido = input("\nInforme o atributo (exatamente como está abaixo) a ser alterado no livro:\n"
                                "titulo || descricao || anolancamento || autor || editora || qtdpaginas || categoria\n"
                                "Atributo escolhido: ")

    novo_valor = {"$set": {atributo_escollhido: input("\nInforme o novo valor para o atributo: ")}}
    mycolLivros.update_one(livro_escolhido, novo_valor)


def excluir(pessoa, tudo):
    if pessoa:
        if tudo:
            mycolPessoa.delete_many({})
        else:
            exibir_registros(True)
            mycolPessoa.delete_one({"_id": ObjectId(input("Informe o ID da pessoa a ser excluída: "))})
    else:
        if tudo:
            mycolLivros.delete_many({})
        else:
            exibir_registros(False)
            mycolLivros.delete_one({"_id": ObjectId(input("Informe o ID do livro a ser excluído: "))})


def consultar(pessoa, tudo):
    if pessoa:
        if tudo:
            pessoas_cadastradas = mycolPessoa.find().sort("name", 1)

            for p in pessoas_cadastradas:
                print(p)

        else:
            filtro = {input(
                "\nInforme o atributo (exatamente como está abaixo) de pessoa a ser utilizado como"
                " parâmetro na consulta:\n"
                "nome || telefone || cidade || endereço || email || nome_pai || nome_mae\n"
                "Atributo escolhido: "): input("Informe o valor do atributo a ser pesquisado: ")}

            for c in mycolPessoa.find(filtro):
                print(c)
    else:
        if tudo:
            livros_cadastrados = mycolLivros.find().sort("titulo", 1)

            for c in livros_cadastrados:
                print(c)

        else:
            filtro = {input(
                "\nInforme o atributo (exatamente como está abaixo) de pessoa a ser utilizado como"
                " parâmetro na consulta:\n"
                "titulo || descricao || anolancamento || autor || editora || qtdpaginas || categoria\n\n"
                "Atributo escolhido: "): input("Informe o valor do atributo a ser pesquisado: ")}

            for c in mycolLivros.find(filtro):
                print(c)


def vazio():
    if mycolPessoa.estimated_document_count() == 0 and mycolLivros.estimated_document_count() == 0:
        print("Não há registros cadastrados!")
        return True


while True:
    time.sleep(1)
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
        if vazio():
            continue
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
        if vazio():
            continue
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
        if vazio():
            continue
        table_consulta = input("\n1 - Consultar pessoa\n"
                               "2 - Consultar livro\n"
                               "Informe qualquer outro caractere para voltar ao menu\n"
                               "Opção escolhida: ")
        if table_consulta == "1":
            opcao = input("\n1 - Consultar todas as pessoas\n"
                          "2 - Consulta personalizada\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                consultar(True, True)
            elif opcao == "2":
                consultar(True, False)

        if table_consulta == "2":
            opcao = input("\n1 - Consultar todos os livros\n"
                          "2 - Consulta personalizada\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                consultar(False, True)
            elif opcao == "2":
                consultar(False, False)
        else:
            continue
    elif option == "0":
        break
    else:
        print("Informe uma opção válida!")

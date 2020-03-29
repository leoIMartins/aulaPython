arq = open('C:\\Python\\Aula 4 - Imprimir nomes em ordem alfabética\\arq.txt', 'r')
informacoes = arq.readlines()

nomes = []
for linha in informacoes:
    nomes.append(linha[2:9])

nomesOrdenados = sorted(nomes)

print("Nomes em ordem alfabetica:\n")
for nome in nomesOrdenados:
    print(nome)

arq.close()

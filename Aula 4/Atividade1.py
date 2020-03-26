arq = open('C:\\Python\\Aula 4\\arq.txt', 'r')
informacoes = arq.readlines()

nomes = []
for linha in informacoes:
    # print(linha[2:14:])
    nomes.append(linha[2:9])

print("Nomes em ordem alfabetica:\n")
print(sorted(nomes))
arq.close()

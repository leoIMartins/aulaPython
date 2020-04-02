arquivo = open('C:\\Python\\Aula 5\\1617FedSchoolCodeList.csv', 'r')

lines = arquivo.readlines()
cidades = []
i = 0

for l in lines:
    coluna = l.split(';')
    if (not cidades.__contains__(coluna[4])):
        cidades.append(coluna[4])
        j = 0
        for la in lines:
            coluna = la.split(';')
            if coluna[4] == cidades[i]:
                j += 1
        print("Cidade %s - %d escolas" % (cidades[i], j))
        i += 1


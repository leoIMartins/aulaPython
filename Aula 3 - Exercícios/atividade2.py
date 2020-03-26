arq = open('C:\\Users\\lmartins8\\projetos\\aulapython01\\Aula 3 - Exercícios\\carros.txt', 'w')
carros = []
carros.append('Gol\n')
carros.append('Uno\n')
carros.append('Palio\n')
carros.append('EcoSport\n')
carros.append('Clio\n')
carros.append('Strada\n')
carros.append('Golf\n')
arq.writelines(carros)
arq.close()

'''arq2 = open('C:\\Python\\Aula 3 - Exercícios\\carros em ordem inversa.txt', 'w')
carrosOrdemInversa = sorted(carros, reverse=True)
arq2.writelines(carrosOrdemInversa)
arq.close'''

arq2 = open('C:\\Python\\Aula 3 - Exercícios\\carros em ordem inversa.txt', 'w')
carrosOrdemInversa = carros[::-1]
arq2.writelines(carrosOrdemInversa)
arq.close

arq3 = open('C:\\Python\\Aula 3 - Exercícios\\carros em ordem alfabetica.txt', 'w')
carrosOrdemAlfabetica = sorted(carros)
arq3.writelines(carrosOrdemAlfabetica)
arq.close

arq4 = open('C:\\Python\\Aula 3 - Exercícios\\carros numerados.txt', 'w')
i = 1
carrosNumerados = []
for cars in carrosOrdemAlfabetica:
    carrosNumerados.append("%d - %s" % (i, cars))
    i += 1
arq4.writelines(carrosNumerados)
arq.close

arq = open('C:\\Users\\lmartins8\\projetos\\aulapython01\\carros.txt', 'w')
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

arq2 = open('C:\\Users\\lmartins8\\projetos\\aulapython01\\carros em ordem inversa.txt', 'w')
carrosOrdemInversa = sorted(carros, reverse=True)
arq2.writelines(carrosOrdemInversa)
arq.close

arq3 = open('C:\\Users\\lmartins8\\projetos\\aulapython01\\carros em ordem alfabetica.txt', 'w')
carrosOrdemAlfabetica = sorted(carros)
arq3.writelines(carrosOrdemAlfabetica)
arq.close

print(carrosOrdemAlfabetica)

i = 0
for cars in carrosOrdemAlfabetica:
    carrosOrdemAlfabetica.insert(i, " - ")
    i += 2
print(carrosOrdemAlfabetica)

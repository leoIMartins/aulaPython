numeros = []

for i in range(6):
    while numeros[i] < 1 or numeros[i] > 60:
        numeros.append(input("Digite o %d número: " % (i)))
print(numeros)
import random

numeros = []
numerosSorteio = []

def escolherNumeros():
    i = 1
    while len(numeros) < 6:
        numero = int(input("\nDigite o %dº número: " % i))
        if numeros.__contains__(numero):
            return print("Os números não podem se repetir")
        elif numero < 1 or numero > 60:
            return print("Informe apenas números entre 1 e 60")
        else:
            numeros.append(numero)
            i += 1


def gerarJogo():
    while len(numerosSorteio) < 6:
        sorteio = random.randint(1, 60)
        if numerosSorteio.__contains__(sorteio):
            break
        else:
            numerosSorteio.append(sorteio)
    return numerosSorteio

escolherNumeros()
sorteioMegaSena = gerarJogo()

print("\nOs números escolhidos foram: " + str(numeros))
print("Os números sorteados foram: " + str(sorteioMegaSena))

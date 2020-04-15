import random

numeros = []
numerosSorteio = []
numerosOrdenados = []
jogosRealizados = []

def escolherNumeros():
    i = 1
    while len(numeros) < 6:
        numero = int(input("\nDigite o %dº número: " % i))
        if numeros.__contains__(numero):
            print("Os números não podem se repetir")
        elif numero < 1 or numero > 60:
            print("Informe apenas números entre 1 e 60")
        else:
            numeros.append(numero)
            i += 1


def gerarJogo():
    if len(numerosSorteio) > 1:
        del numerosSorteio[:]
    while len(numerosSorteio) < 6:
        sorteio = random.randint(1, 60)
        if numerosSorteio.__contains__(sorteio):
            continue
        else:
            numerosSorteio.append(sorteio)
    if jogosRealizados.__contains__(sorted(numerosSorteio)):
        gerarJogo()
    else:
        jogosRealizados.append(sorted(numerosSorteio))
        return numerosSorteio


def tentaAcertar():
    escolherNumeros()
    while sorted(numeros) != sorted(numerosSorteio):
        gerarJogo()
        numerosOrdenados = sorted(numerosSorteio)
        print(numerosOrdenados)
    print("VOCÊ GANHOU NA MEGA SENA!!!!!")
    print("\n\nJogo feito: " + str(sorted(numeros)))
    print("Números da mega sena: " + str(numerosOrdenados))


tentaAcertar()

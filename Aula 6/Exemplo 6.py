import time
import random

numero = 0
while numero < 1 or numero > 5:
    numero = int(input("Informe um número de 1 a 5: "))

print("PROCESSANDO....")
time.sleep(1)
print("..........")
time.sleep(2)

numeroRandomico = random.randint(1, 5)

if numero == numeroRandomico:
    print("PARABÉNS!")
else:
    print("Número sorteado: " + str(numeroRandomico))
    print("Número escolhido: " + str(numero))

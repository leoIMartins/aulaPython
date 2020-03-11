menor = 0
maior = 0

a = int(input("Informe o primeiro numero: "))
menor = a
maior = a

b = int(input("Informe o segundo numero: "))
if b < menor:
    menor = b
if b > maior:
    maior = b

c = int(input("Informe o terceiro numero: "))
if c < menor:
    menor = c
if c > maior:
    maior = c

print("\nMaior: ", maior)
print("Menor: ", menor)
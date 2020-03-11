valor = -1
salario = -1
anos = -1
parcela = 0

while(valor < 0):
    valor = float(input("Informe o valor do imovel: R$"))
    if(valor < 0):
        print("O valor do imovel nao pode ser negativo!\n")

while(salario < 0):
    salario = float(input("Informe o valor do seu salario: R$"))
    if(salario < 0):
        print("O valor do salario nao pode ser negativo!\n")

while(anos < 0):
    anos = float(input("Informe quantos anos tem para pagar: "))
    if(anos < 0):
        print("A quantidade de anos nao pode ser negativa!\n")

parcela = valor / (anos*12)

print("\nValor da parcela: R$%.2f" % (parcela))
print("Meses para pagar: %.0f" % (anos*12))

if(parcela > (salario*0.3)):
    print("\nO valor da parcela e maior que 30% do salario!")
else:
    print("\nA compra pode ser realizada!")

print("Parcela/Salario = %f" % ((parcela/salario)*100))
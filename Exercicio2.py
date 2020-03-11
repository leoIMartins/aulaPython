a = 0
b = 0
c = 0
while a<=0:
    a = int(input("Informe o valor do lado A: "))
    if a<=0:
        print("A medida de um lado não pode ser menor ou igual a zero!\n")

while b<=0:
    b = int(input("Informe o valor do lado B: "))
    if b<=0:
        print("A medida de um lado não pode ser menor ou igual a zero!\n")

while c<=0:
    c = int(input("Informe o valor do lado C: "))
    if c<=0:
        print("A medida de um lado não pode ser menor ou igual a zero!\n")

print("\nLado A = ", a)
print("Lado B = ", b)
print("Lado C = ", c)

if ((a+b<=c) or (a+c<=b) or (b+c<=a)):
    print("\nNão é um Triângulo! A soma entre dois lados é menor ou igual ao terceiro")
        
elif ((a==b) & (a==c) & (b==c)):
	print("\nTriângulo equilátero\n")
    
elif ((a!=b) & (a!=c) & (b!=c)):
    print("\nTriângulo escaleno\n")
        
else:
    print("\nTriângulo isósceles\n")
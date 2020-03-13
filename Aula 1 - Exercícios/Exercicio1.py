import math
print("ax^2 + bx + c = 0")

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))

print("\nA= ", a)
print("B= ", b)
print("C= ", c)

delta = b**2 - 4*a*c

print("\nDelta = ", delta)

if delta > 0:
    print("\nDuas soluções para a equação:\n")
    x1 = (-b + math.sqrt(delta)) / 2*a
    x2 = (-b - math.sqrt(delta)) / 2*a

    print("\nX1 = ", x1)
    print("X2 = ", x2)

elif delta == 0:
    print("\nHá apenas uma solução para a equação:\n")
    x = (-b) / (2*a)
    
    print("\nX = ", x)
else:
    print("\nNão há solução real!\n")
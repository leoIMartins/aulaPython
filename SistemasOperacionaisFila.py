import time

fila = ["1", "2", "3", "4", "5", "6"]

for f in fila:
    time.sleep(1)
    print("Vetor atual: " + str(fila))
    time.sleep(1)
    print("Executando o processo " + fila[5])
    time.sleep(1)
    print("...........................................")
    fila.insert(0, fila[5])
    del fila[6]

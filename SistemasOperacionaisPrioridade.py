import time
priorityOrder = ["High", "Medium", "Low"]
processos = ["Processo 1 High Priority", "Processo 2 Medium Priority", "Processo 3 High Priority",
             "Processo 4 Medium Priority", "Processo 5 Medium Priority", "Processo 6 Low Priority",
             "Processo 7 Medium Priority", "Processo 8 High Priority"]

i = 0
for j in range(3):
    for pr in processos:
        if pr.__contains__(priorityOrder[i]):
            time.sleep(1)
            print(".............................")
            time.sleep(1)
            print("Executando: " + pr)
            time.sleep(2)
    i += 1

nomeCompleto = input("Informe seu nome completo: ")


def minusculo():
    return print("Nome completo em minúsculo: " + nomeCompleto.lower())


def maiusculo():
    return print("Nome completo em MAIÚSCULO: " + nomeCompleto.upper())


def nome_completo_sem_espacos():
    i = 0
    for letra in nomeCompleto.strip():
        if letra != " ":
            i += 1
    return print("O nome completo contém %d letras" % i)


def primeiro_nome():
    j = 0
    for letra in nomeCompleto.strip():
        if letra == " ":
            break
        j += 1
    return print("O primeiro nome contém %d letras" % j)


minusculo()
maiusculo()
nome_completo_sem_espacos()
primeiro_nome()

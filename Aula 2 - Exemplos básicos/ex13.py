#Exemplo13
arq = open('C:\\Users\\lmartins8\\projetos\\aulapython01\\Aula 2 - Exemplos básicos\\lista.txt', 'w')
texto = []
texto.append('Lista de Alunos\n')
texto.append('---\n')
texto.append('Joao da Silva\n')
texto.append('José Lima\n')
texto.append('Maria das Dores')
arq.writelines(texto)
arq.close()

arq = open('C:\\Users\\lmartins8\\projetos\\aulapython01\\Aula 2 - Exemplos básicos\\lista.txt', 'r')
texto = arq.read()
print(texto)
arq.close()

arq = open('C:\\Users\\lmartins8\\projetos\\aulapython01\\Aula 2 - Exemplos básicos\\lista.txt', 'r')
texto = arq.readlines()
for linha in texto:
    print(linha)
arq.close()
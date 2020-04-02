arquivo = open('C:\\Python\\Aula 5\\1617FedSchoolCodeList.csv', 'r')

lines = arquivo.readlines()

for l in lines:
    coluna = l.split(';')
    print("ID: ", coluna[0])
    print("SchoolCode: ", coluna[1])
    print("SchoolName: ", coluna[2])
    print("*******************************")
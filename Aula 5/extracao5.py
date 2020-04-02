arquivo = open('C:\\Python\\Aula 5\\1617FedSchoolCodeList.csv', 'r')

lines = arquivo.readlines()

for l in lines:
    coluna = l.split(';')

    if coluna[6] == "44106":
        print("SchoolName: ", coluna[2])
        print("City: ", coluna[4])
        print("StateCode: ", coluna[5])
        print("*******************************")
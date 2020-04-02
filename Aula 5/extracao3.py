arquivo = open('C:\\Python\\Aula 5\\1617FedSchoolCodeList.csv', 'r')

lines = arquivo.readlines()

for l in lines:
    coluna = l.split(';')
    schoolName = coluna[2]
    if schoolName[0] == "A":
        print("ID: ", coluna[0])
        print("SchoolCode: ", coluna[1])
        print("SchoolName: ", coluna[2])
        print("Address: ", coluna[3])
        print("City: ", coluna[4])
        print("StateCode: ", coluna[5])
        print("ZipCode: ", coluna[6])
        print("Province: ", coluna[7])
        print("Country: ", coluna[8])
        print("PostalCode: ", coluna[9])
        print("*******************************")
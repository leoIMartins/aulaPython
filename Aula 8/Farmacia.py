import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbatividade"]
mycolFarmacia = mydb["farmacia"]


class Farmacia:

    def __init__(self, descricao, qtd_funcionarios, qtd_medicamentos, endereco, telefone, cidade, estado):
        self.descricao = descricao
        self.qtd_funcionarios = qtd_funcionarios
        self.qtd_medicamentos = qtd_medicamentos
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado
        farmacia = {"descricao": descricao, "qtd_funcionarios": qtd_funcionarios, "qtd_medicamentos": qtd_medicamentos,
                    "endereco": endereco, "telefone": telefone, "cidade": cidade, "estado": estado}
        mycolFarmacia.insert_one(farmacia)

    def set_descricao(self, descricao):
        self.descricao = descricao

    def set_qtd_funcionarios(self, qtd_funcionarios):
        self.qtd_funcionarios = qtd_funcionarios

    def set_qtd_medicamentos(self, qtd_medicamentos):
        self.qtd_medicamentos = qtd_medicamentos

    def set_endereco(self, endereco):
        self.endereco = endereco

    def set_telefone(self, telefone):
        self.telefone = telefone

    def set_cidade(self, cidade):
        self.cidade = cidade

    def set_estado(self, estado):
        self.estado = estado

    def get_descricao(self):
        return self.descricao

    def get_qtd_funcionarios(self):
        return self.qtd_funcionarios

    def get_qtd_medicamentos(self):
        return self.qtd_medicamentos

    def get_endereco(self):
        return self.endereco

    def get_telefone(self):
        return self.telefone

    def get_cidade(self):
        return self.cidade

    def get_estado(self):
        return self.estado


from django.db import models


class Comida(models.Model):
    tipoComida = models.CharField(max_length=20)
    descricao = models.CharField(max_length=50)
    quantidade = models.DecimalField(max_length=3)
    opcoes = models.CharField(max_length=50)
    valorCalorico = models.DecimalField(max_length=10)
    salada = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

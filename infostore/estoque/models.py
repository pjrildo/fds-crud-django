from django.db import models


class Fornecedor(models.Model):
    nome_fantasia = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True, blank=False)
    telefone = models.CharField(max_length=15, unique=True, blank=False)

    def __str__(self):
        return self.nome_fantasia


class Categoria(models.Model):
    nome = models.CharField(max_length=30, unique=True, blank=False)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

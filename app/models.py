from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null= False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=100, null=False, blank=False)

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null= False, blank=False)
    cpf = models.IntegerField(max_length=11, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    remuneracao = models.IntegerField(null=False, blank=False)
    
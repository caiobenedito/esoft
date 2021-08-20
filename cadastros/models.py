# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome")
    login = models.EmailField(max_length=150, verbose_name="Login")
    senha = models.CharField(max_length=150, verbose_name="Senha")
    cep = models.IntegerField()
    endereco = models.CharField(max_length=150, verbose_name="Endereço")
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50, verbose_name="Complemento")
    bairro = models.CharField(max_length=150, verbose_name="Bairro")
    cidade = models.CharField(max_length=150, verbose_name="Cidade")
    estado = models.CharField(max_length=150, verbose_name="Estado")

    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {}".format(self.nome,self.login,self.senha,self.cep,self.endereco,self.numero,self.complemento,self.bairro,self.cidade,self.estado)

class Produto(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150, verbose_name="Nome")
    preco = models.FloatField(verbose_name="Preço")
    estoque = models.IntegerField(verbose_name="Estoque")

    def __str__(self):
        return "{} {} {} {}".format(self.id,self.nome,self.preco,self.estoque)




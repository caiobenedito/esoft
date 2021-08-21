# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from  rest_framework import serializers,generics
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
# Create your models here.
class Usuario(models.Model):

     nome = models.CharField(max_length=150, verbose_name="Nome")
     username = models.OneToOneField(User, on_delete=models.CASCADE,null=True,related_name='usuario')
     cep = models.IntegerField()
     endereco = models.CharField(max_length=150, verbose_name="Endereço")
     numero = models.IntegerField()
     complemento = models.CharField(max_length=50, verbose_name="Complemento",blank=True)
     bairro = models.CharField(max_length=150, verbose_name="Bairro")
     cidade = models.CharField(max_length=150, verbose_name="Cidade")
     estado = models.CharField(max_length=150, verbose_name="Estado")


def __str__(self):
    return "{} {}  {} {} {} {} {} {} {}".format(self.nome, self.username, self.cep, self.endereco, self.numero,
                                                self.complemento, self.bairro, self.cidade, self.estado)


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields=('nome','username','cep','endereco','numero','complemento','bairro','bairro','cidade','estado'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','email','usuario')
    usuarios = UsuarioSerializer(many=True)

class inventroyList(generics.ListCreateAPIView):
    #queryset = User.objects.prefetch_related('usuario')
    queryset= User.objects.prefetch_related('usuarios')
    print(str(queryset.query))
    # serializer_class = UserSerializer
    # queryset = self.queryset()
    #obj = get_object_or_404(queryset)
    #print(obj)

    def __str__(self):
        queryset = self.queryset()
        obj = get_object_or_404(queryset)
        return obj


# def __str__(self):
#
#     return "%s's profile" % self.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = Usuario.objects.get_or_create(username=instance)

post_save.connect(create_user_profile, sender=User)
#username.get_profile().whatever

# class Usuario(models.Model):
#     nome = models.CharField(max_length=150, verbose_name="Nome")
#     #username = models.ForeignKey(AUTH_USER_MODEL,primary_key=True,unique=True)
#     username = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,)
#     #username = models.EmailField(max_length=150, verbose_name="Login", unique=True)
#     #password = models.CharField(max_length=150, verbose_name="Senha")
#     cep = models.IntegerField()
#     endereco = models.CharField(max_length=150, verbose_name="Endereço")
#     numero = models.IntegerField()
#     complemento = models.CharField(max_length=50, verbose_name="Complemento",blank=True)
#     bairro = models.CharField(max_length=150, verbose_name="Bairro")
#     cidade = models.CharField(max_length=150, verbose_name="Cidade")
#     estado = models.CharField(max_length=150, verbose_name="Estado")
#
#     def __str__(self):
#         return "{} {}  {} {} {} {} {} {} {}".format(self.nome, self.username,  self.cep, self.endereco, self.numero, self.complemento, self.bairro, self.cidade, self.estado)

class Produto(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    nome = models.CharField(max_length=150, verbose_name="Nome",unique=True)
    preco = models.FloatField(verbose_name="Preço")
    estoque = models.IntegerField(verbose_name="Estoque")

    def __str__(self):
        return "{} {} {} {}".format(self.id,self.nome,self.preco,self.estoque)




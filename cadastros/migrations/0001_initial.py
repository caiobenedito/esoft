# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-19 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('preco', models.FloatField(verbose_name='Pre\xe7o')),
                ('estoque', models.IntegerField(verbose_name='Estoque')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('login', models.EmailField(max_length=150, verbose_name='Login')),
                ('senha', models.CharField(max_length=150, verbose_name='Senha')),
                ('cep', models.IntegerField()),
                ('endereco', models.CharField(max_length=150, verbose_name='Endere\xe7o')),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=50, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=150, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=150, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=150, verbose_name='Estado')),
            ],
        ),
    ]

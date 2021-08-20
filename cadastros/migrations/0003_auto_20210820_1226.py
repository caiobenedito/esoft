# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-20 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_auto_20210820_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='login',
            field=models.EmailField(max_length=150, unique=True, verbose_name='Login'),
        ),
    ]

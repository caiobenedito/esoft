# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-20 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='complemento',
            field=models.CharField(blank=True, max_length=50, verbose_name='Complemento'),
        ),
    ]
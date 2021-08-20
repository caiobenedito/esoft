# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#importar as classes
from .models import  Usuario, Produto

from django.contrib import admin

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Produto)
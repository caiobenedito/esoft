# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from django.shortcuts import render

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class SobreView(TemplateView):
    template_name = "username.html"

class CadastrarView(TemplateView):
    template_name = 'cadastrar.html'

class HomeView(TemplateView):
    template_name = 'home.html'

class ProdutosView(TemplateView):
    template_name = 'produtos.html'
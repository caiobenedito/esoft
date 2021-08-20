# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import  CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import Usuario,Produto
from django.urls import  reverse_lazy

# Create your views here.


class UsuarioCraate(CreateView):
    model = Usuario
    fields = ['nome','login','senha','cep','endereco','numero','complemento','bairro','cidade','estado']
    template_name =  'form-cadastrar-usuario.html'
    success_url = reverse_lazy('listar-usuarios')

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['id','nome','preco','estoque']
    template_name = 'form-cadastrar-produto.html'
    success_url = reverse_lazy('listar-produtos')

##################### update ########################

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = ['nome', 'login', 'senha', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado']
    template_name = 'form-cadastrar-usuario.html'
    success_url = reverse_lazy('listar-usuarios')

class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['id','nome','preco','estoque']
    template_name = 'form-cadastrar-produto.html'
    success_url = reverse_lazy('listar-produtos')

##################### update ########################

class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-usuarios')

class ProdutoDelete(DeleteView):
    model = Produto
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-produtoso')

##################### update ########################

class UsuarioList(ListView):
    model = Usuario
    template_name = 'usuario.html'
    success_url = reverse_lazy('listar-usuarios')

class ProdutoList (ListView):
    model = Produto
    template_name = 'produto.html'
    success_url = reverse_lazy('listar-produtoso')
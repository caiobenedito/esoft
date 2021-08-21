# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import  CreateView,UpdateView,DeleteView,FormMixin
from extra_views import CreateWithInlinesView,ModelFormSetView,InlineFormSetView
from django.views.generic.list import ListView
from .models import Usuario,Produto,UsuarioSerializer,UserSerializer,inventroyList
from django.contrib.auth.models import User
from django.urls import  reverse_lazy
from django.db import models

# Create your views here.


# class UsuarioCraate(CreateView):
#     model = Usuario,User
#     fields = ['nome','username','User.password','cep','endereco','numero','complemento','bairro','cidade','estado']
#     template_name =  'form-cadastrar-usuario.html'
#     success_url = reverse_lazy('listar-usuarios')


class UsuarioCraate(ListView):
    model = Usuario
    fields = ['nome', 'username', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade',
              'estado']
    template_name = 'form-cadastrar-usuario.html'

class UpdateOrderView(CreateWithInlinesView):
    model = User
    inlines = [UsuarioCraate,]
    success_url = reverse_lazy('listar-usuarios')


    # template_name = 'form-cadastrar-usuario.html'
    # context_object_name = 'character_series_list'
    #
    # def get_context_data(self, **kwargs):
    #     context=super(UsuarioCraate,self).get_context_data(**kwargs)
    #     context['password'] = User.password()
    #
    #     return  context

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['id','nome','preco','estoque']
    template_name = 'form-cadastrar-produto.html'
    success_url = reverse_lazy('listar-produtos')

##################### update ########################

# class UsuarioUpdate(InlineFormSetView):
#     model = Usuario
#     form_class = User
#     template_name = 'form-cadastrar-usuario.html'
#     success_url = reverse_lazy('listar-usuarios')


class UsuarioUpdate(UpdateView):
     model = Usuario
     fields = ['nome', 'username','cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado']
     template_name = 'form-cadastrar-usuario.html'
     success_url = reverse_lazy('listar-usuarios')

class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['id','nome','preco','estoque']
    template_name = 'form-cadastrar-produto.html'
    success_url = reverse_lazy('listar-produtos')

##################### Delete ########################

class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-usuarios')

class ProdutoDelete(DeleteView):
    model = Produto
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-produtoso')

##################### ListView ########################

# class UsuarioList(ListView):
#     model = Usuario
#     template_name = 'usuario.html'
#     success_url = reverse_lazy('listar-usuarios')

class UsuarioList(ListView):
    model = inventroyList
    template_name = 'usuario.html'
    success_url = reverse_lazy('listar-usuarios')


# class UsuarioList(ListView,):
#     queryset = User.objects.prefetch_related('usuario')
#     serializer_class = UserSerializer
#
#     model = serializer_class
#     context_object_name = 'usuario'
#     template_name = 'usuario.html'
#     success_url = reverse_lazy('listar-usuarios')



class ProdutoList (ListView):
    model = Produto
    template_name = 'produto.html'
    success_url = reverse_lazy('listar-produtoso')
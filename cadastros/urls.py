#from django.urls  import path
from django.conf.urls import url,include
from .views import UsuarioCraate,ProdutoCreate,UsuarioUpdate,ProdutoUpdate,\
    UsuarioDelete,ProdutoDelete,UsuarioList,ProdutoList

urlpatterns = [
    url('cadastrar/usuario/', UsuarioCraate.as_view(), name='cadastrar-usuario'),
    url('cadastrar/produto/', ProdutoCreate.as_view(), name='cadastrar-produto'),

    url(r'editar/usuario/(?P<pk>\d+)/$',UsuarioUpdate.as_view(),name='editar-usuario'),
    url(r'editar/produto/(?P<pk>\d+)/$',ProdutoUpdate.as_view(),name='editar-produto'),

    #url(r'editar/usuario/(?P<pk>\d+)/$',UsuarioUpdate.as_view(),name='editar-usuario'),
    #url(r'editar/produto/(?P<pk>\d+)/$',ProdutoUpdate.as_view(),name='editar-produto'),

    url(r'excluir/usuario/(?P<pk>\d+)/$',UsuarioDelete.as_view(),name='excluir-usuario'),
    url(r'excluir/produto/(?P<pk>\d+)/$',ProdutoDelete.as_view(),name='excluir-produto'),

    url('listar/usuarios', UsuarioList.as_view(),name='listar-usuarios'),
    url('listar/produtos', ProdutoList.as_view(),name='listar-produtos'),
]
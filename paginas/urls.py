#from django.urls  import path
from django.conf.urls import url,include
from .views import IndexView, SobreView,CadastrarView,HomeView,ProdutosView

urlpatterns = [
    url('inicio/', IndexView.as_view(), name='inicio'),
    url('login/', SobreView.as_view(), name='login'),
    #url('cadastrar/', CadastrarView.as_view(), name='cadastrar'),
    url('home/', HomeView.as_view(), name='home'),
    url('produtos/', ProdutosView.as_view(), name='produtos'),

]

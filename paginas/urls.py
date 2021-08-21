#from django.urls  import path
from django.conf.urls import url,include
from .views import IndexView, SobreView,CadastrarView,HomeView,ProdutosView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('inicio/', IndexView.as_view(), name='inicio'),
    #url('username/', SobreView.as_view(), name='username'),
    #url('cadastrar/', CadastrarView.as_view(), name='cadastrar'),
    url('home/', HomeView.as_view(), name='home'),
    url('produtos/', ProdutosView.as_view(), name='produtos'),
    url('login/', auth_views.LoginView.as_view(
        template_name='form_login.html/'
    ), name='login'),
    url('logout/', auth_views.LogoutView.as_view(), name='logout'),


]

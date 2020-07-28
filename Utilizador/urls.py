"""INSJCM -> Igreja do Nosso senhor Jesus cristo no Mundo URL """
from django.urls import path, re_path
from . import views


app_name = 'Utilizador'
urlpatterns = [
    path('', views.login_utilizador, name='login'),
    path('login_utilizador', views.login_utilizador, name='login-utilizador'),
]

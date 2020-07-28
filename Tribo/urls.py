"""INSJCM -> Igreja do Nosso senhor Jesus cristo no Mundo URL """
from django.urls import path, re_path
from . import views


app_name = 'Tribo'
urlpatterns = [
    path('registar_cadastro_tribo', views.registar_cadastro_tribo, name='registar-tribo'),
]

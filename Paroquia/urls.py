"""INSJCM -> Igreja do Nosso senhor Jesus cristo no Mundo URL """
from django.urls import path, re_path
from . import views


app_name = 'Paroquia'
urlpatterns = [
    path('registar_cadastro_paroquia', views.registar_cadastro_paroquia, name='registar-paroquia'),
]

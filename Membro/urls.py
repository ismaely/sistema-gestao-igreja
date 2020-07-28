"""INSJCM -> Igreja do Nosso senhor Jesus cristo no Mundo URL """
from django.urls import path, re_path
from . import views


app_name = 'Membro'
urlpatterns = [
    path('registar_cadastro_membro/', views.registar_cadastro_membro, name='cadastro-membro'),
]

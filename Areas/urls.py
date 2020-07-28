"""INSJCM -> Igreja do Nosso senhor Jesus cristo no Mundo URL """
from django.urls import path, re_path
from . import views


app_name = 'Areas'
urlpatterns = [
    path('registar_cadastro_area', views.registar_cadastro_area, name='registar-area'),
]

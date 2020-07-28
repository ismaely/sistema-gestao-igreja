"""INSJCM -> Igreja do Nosso senhor Jesus cristo no Mundo URL """
from django.urls import path, re_path
from . import views


app_name = 'Catedral_Central'
urlpatterns = [
    path('home_central', views.home_central, name='home-central'),
]

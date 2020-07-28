"""SGT_INSJCM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('Utilizador.urls')),
    path('Catedral_Central/', include('Catedral_Central.urls')),
    path('Membro/', include('Membro.urls')),
    path('Classe/', include('Classe.urls')),
    path('Paroquia/', include('Paroquia.urls')),
    path('Tribo/', include('Tribo.urls')),
    path('Areas/', include('Areas.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

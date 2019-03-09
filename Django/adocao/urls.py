from django.urls import path

from .views import *

urlpatterns = [
#path('caminho url', classeViewCriada, name="nome url")
    path('inicio/', PaginaInicialView.as_view(), name="index"),
    path('sobre/', PaginaSobreView.as_view(), name="sobre"),
]

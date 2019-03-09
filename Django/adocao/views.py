from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class PaginaInicialView(TemplateView):
    template_name = "index.html"

class PaginaSobreView(TemplateView):
    template_name ="sobre.html"

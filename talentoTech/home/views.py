"""
    Autor:
"""
from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    """
        Autor:
    """
    template_name = "home/index.html"

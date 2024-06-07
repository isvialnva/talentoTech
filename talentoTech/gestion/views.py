"""
    Autor:
"""
from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DeleteView, UpdateView)
from django.views.generic.detail import DetailView
from talentoTech.settings import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy


@login_required(login_url=LOGOUT_REDIRECT_URL)
def gestion_index(request):
    """
        Autor:
    """
    context = {
        'username': request.user.username
    }
    return render(request, 'gestion/index.html', context)

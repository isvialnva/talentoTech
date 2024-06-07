"""
    Autor:
"""
from django.urls import path, include
from .views import gestion_index

urlpatterns = [
    path('indexadmin', gestion_index, name='indexadmin'),
]

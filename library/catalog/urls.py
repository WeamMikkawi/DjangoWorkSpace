"""
Specify the urls for catalog app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.notImplmented, name='catalog')
]
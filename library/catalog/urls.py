"""
Specify the urls for catalog app
"""
from django.urls import path
from . import views
#from django.views.generic import RedirectView

urlpatterns = [
    path('', views.notImplmented, name='catalog'),
]
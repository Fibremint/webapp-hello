'''
Created on Sep 12, 2015

@author: fibremint
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.hello)               
]
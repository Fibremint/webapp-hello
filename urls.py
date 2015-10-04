'''
Created on Sep 12, 2015

@author: fibremint
'''
from django.conf.urls import include, url
from rest_framework import routers

from .views import JobViewSet, index


router = routers.DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^$', index, name='hello_index'),
]
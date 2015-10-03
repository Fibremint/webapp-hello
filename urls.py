'''
Created on Sep 12, 2015

@author: fibremint
'''
from django.conf.urls import include, url
from rest_framework import routers

from hello_app.views import JobViewSet


router = routers.SimpleRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
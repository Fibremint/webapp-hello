from rest_framework import viewsets, permissions

from hello_app.models import Job
from hello_app.serializers import JobSerializer
from django.shortcuts import render_to_response
from django.template.context import RequestContext


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.AllowAny,)
    
def index(request):
    return render_to_response('hello_app/index.html', RequestContext(request))
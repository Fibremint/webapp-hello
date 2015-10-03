from rest_framework import viewsets, permissions

from hello_app.models import Job
from hello_app.serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.AllowAny(),)
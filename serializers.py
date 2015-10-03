from rest_framework import serializers

from hello_app.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('name', 'description',)
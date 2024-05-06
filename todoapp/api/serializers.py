from rest_framework import serializers
from base.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'contents', 'deadline', 'completed', 'user']

from rest_framework import serializers

# Project modules
from apps.task.models import Task

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['Task_name', 'Due_date','Employee_name','Priority']

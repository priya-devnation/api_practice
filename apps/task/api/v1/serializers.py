from rest_framework import serializers

# Project modules
from apps.task.models import Task

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','uuid','Task_name', 'Task_description', 'Task_status', 'Due_date','Employee_name','Tags','Priority']


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['Task_name', 'Due_date','Employee_name','Priority']


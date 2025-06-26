# Restframework modules
from rest_framework import serializers

# Project modules
from apps.task.models import Task

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','Task_name', 'Task_description', 'Task_status', 'Due_date','Employee_name','Tags','Priority']

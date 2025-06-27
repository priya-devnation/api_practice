from rest_framework import serializers

# Project modules
from apps.task.models import Task

class TaskCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','uuid','task_name', 'task_description', 'task_status', 'due_date','employee_name','tags','priority']


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_name', 'due_date','employee_name','priority']


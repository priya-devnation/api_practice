#Restframework modules
from rest_framework import serializers

#project modules
from apps.todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','title','description','is_completed']
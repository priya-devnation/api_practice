# Restframework modules
from rest_framework import serializers

# Project modules
from apps.students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course', 'marks']
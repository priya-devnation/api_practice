# Restframework modules
from rest_framework import serializers

# Project modules
from apps.employee.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','Employee_name','Employee_role','Employee_email']

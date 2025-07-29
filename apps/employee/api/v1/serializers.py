# Restframework modules
from rest_framework import serializers

# Project modules
from apps.employee.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','uuid','employee_name','employee_role','employee_email']



    def validate_email(self, value):
        if Employee.objects.filter(employee_email=value).exists():
            raise serializers.ValidationError("A user with this email id already exists")
        return value


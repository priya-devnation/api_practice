# Restframework modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

# Project modules
from apps.employee.models import Employee
from .serializers import EmployeeSerializer



# view for creating and listing employees
class EmployeeListCreateAPIView(APIView):
    serializer_class = EmployeeSerializer

    def get(self, request):
        try:
            employee = Employee.objects.only('id','uuid','employee_name','employee_role','employee_email').all()
            serializer = self.serializer_class(employee, many=True)
            return Response(serializer.data)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# view for retrieving, updating and deleting a specific employee
class EmployeeRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = EmployeeSerializer

    def get(self, request, uuid):
        try:
            employee = Employee.objects.get(uuid=uuid)
            serializer = self.serializer_class(employee)
            return Response(serializer.data)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, uuid):
        try:
            employee = Employee.objects.get(uuid=uuid)
            serializer = self.serializer_class(employee, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, uuid):
        try:
            Employee.objects.get(uuid=uuid).delete()
            return Response({"detail":"employee deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
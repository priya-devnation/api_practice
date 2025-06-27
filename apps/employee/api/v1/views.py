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
            employee = Employee.objects.only('id','uuid','Employee_name','Employee_role','Employee_email').all()
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

    def get(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = self.serializer_class(employee)
            return Response(serializer.data)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = self.serializer_class(employee, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            Employee.objects.get(pk=pk).delete()
            return Response({"detail":"employee deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
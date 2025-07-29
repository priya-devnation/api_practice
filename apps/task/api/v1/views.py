# Restframework modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

# Project modules
from apps.task.models import Task
from .serializers import TaskCreateUpdateSerializer,TaskListSerializer





# view for creating tasks
class TaskCreateAPIView(APIView):
    serializer_class = TaskCreateUpdateSerializer
    
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
        
class TaskListAPIView(APIView):
    serializer_class = TaskListSerializer

    def get(self, request):
        try:
            task = Task.objects.only('uuid','task_name','due_date','employee_name','priority').all()
            serializer = self.serializer_class(task, many=True)
            return Response(serializer.data)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# view for retrieving, updating and deleting a specific Student
class TaskRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = TaskCreateUpdateSerializer

    def get(self, request, uuid):
        try:
            task = Task.objects.get(uuid=uuid)
            serializer = self.serializer_class(task)
            return Response(serializer.data)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, uuid):
        try:
            task = Task.objects.get(uuid=uuid)
            serializer = self.serializer_class(task, data=request.data,partial=True)
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
            Task.objects.get(uuid=uuid).delete()
            return Response({"detail":"task deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
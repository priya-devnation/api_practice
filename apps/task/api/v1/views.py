# Restframework modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

# Project modules
from apps.task.models import Task
from .serializers import TaskSerializer



# view for creating and listing tasks
class TaskListCreateAPIView(APIView):
    serializer_class = TaskSerializer

    def get(self, request):
        try:
            task = Task.objects.only('id','Task_name','Task_description','Task_status','Due_date').all()
            serializer = self.serializer_class(task, many=True)
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

# view for retrieving, updating and deleting a specific Student
class TaskRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = TaskSerializer

    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serializer = self.serializer_class(task)
            return Response(serializer.data)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serializer = self.serializer_class(task, data=request.data,partial=True)
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
            Task.objects.get(pk=pk).delete()
            return Response({"detail":"task deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
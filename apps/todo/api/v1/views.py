# Restframework modules

from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status
from rest_framework.exceptions import ValidationError

#project Modules
from apps.todo.models import Todo
from .serializers import TodoSerializer



#view for listing and creating data in todo

class TodoListCreateAPIView(APIView):
    serializer_class =TodoSerializer
    
    def get(self,request):
        try:
            todo = Todo.objects.only('id','title','description','is_completed').all()
            serializer = self.serializer_class(todo, many=True)
            return Response(serializer.data)
        except ValidationError as ve:
            raise ve
        except Exception as e: # Handle other exceptions
            return Response({"detail":str (e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as ve:
            raise ve
        except Exception as e: # Handle other exceptions
            return Response({"detail":str (e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
         # view for retrieving, updating and deleting data from todo

class TodoRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = TodoSerializer
        
    def get(self, request, pk):
            try:
                todo = Todo.objects.get(pk=pk)
                serializer = self.serializer_class(todo)
                return Response(serializer.data)
            except ValidationError as ve:
                raise ve
            except Exception as e: # Handle other exceptions
                return Response({"detail":str (e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def patch(self, request,pk):
        try:
            todo = Todo.objects.get(pk=pk)
            serializer = self.serializer_class(todo, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as ve:
            raise ve
        except Exception as e: # Handle other exceptions
            return Response({"detail":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk).delete()
            return Response({"detail":"data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
                
        
        
            

        
    

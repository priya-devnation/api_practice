#rest framework modules 
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status
from rest_framework.exceptions import ValidationError

#project modules
from apps.event.models import Event
from .serializers import EventSerializer


#view for listing and creating
class EventListCreateAPIView(APIView):
    serializer_class = EventSerializer
    
    def get(self, request):
        try:
            event = Event.objects.only('event_name','event_date', 'location','capacity').all()
            serializer = self.serializer_class(event, many=True)
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


#view for retrieving updating and deleting
class EventRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = EventSerializer

    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            serializer = self.serializer_class(event)
            return Response(serializer.data)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def patch(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            serializer = self.serializer_class(event, data=request.data,partial=True)
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
            Event.objects.get(pk=pk).delete()
            return Response({"detail":"event deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
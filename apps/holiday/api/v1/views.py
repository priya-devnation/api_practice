# Project modules
from apps.holiday.models import HolidayMaster
from .serializers import HolidayMasterSerializer

# Third party modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

# view for creating and listing holiday
class HolidayListCreateAPIView(APIView):
    serializer_class = HolidayMasterSerializer

    def get(self, request):
        try:
            holiday = HolidayMaster.objects.only('id', 'label', 'start_datetime', 'end_datetime').all()
            serializer = self.serializer_class(holiday, many=True)
            return Response(serializer.data)
        
        except ValidationError as ve: # Handle validation errors
            raise ve
        
        except Exception as e: # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except ValidationError as ve: # Handle validation errors
            raise ve
        
        except Exception as e: # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# view for retrieving, updating and deleting holiday
class HolidayRetrieveUpdateDestroyAPIView(APIView):
    serializer_class = HolidayMasterSerializer

    def get(self, request, pk, *args, **kwargs):
        try:
            holiday = HolidayMaster.objects.get(pk=pk)
            serializer = self.serializer_class(holiday)
            return Response(serializer.data)

        except ValidationError as ve: # Handle validation errors
            raise ve
        
        except Exception as e: # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk, *args, **kwargs):
        try:
            holiday = HolidayMaster.objects.get(pk=pk)
            serializer = self.serializer_class(holiday, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        except ValidationError as ve: # Handle validation errors
            raise ve
        
        except Exception as e: # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, pk, *args, **kwargs):
        try:
            HolidayMaster.objects.get(pk=pk).delete()
            return Response({"detail":"Holiday deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        
        except ValidationError as ve: # Handle validation errors
            raise ve
        
        except Exception as e: # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
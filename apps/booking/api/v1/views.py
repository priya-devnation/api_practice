#rest framework modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


#project modules
from apps.booking.models import Booking
from .serializers import BookingSerializer

#view for listing and creating Booking
class BookingListCreateAPIView(APIView):
    serializer_class = BookingSerializer

    def get(self, request):
        try:
            booking = Booking.objects.only('name','email', 'ph_no', 'event', 'booked_at').all()
            serializer = self.serializer_class(booking, many=True)
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


#view for retrieving updating and deleting Booking
class BookingRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = BookingSerializer

    def get(self, request, pk):
        try:
            booking = Booking.objects.get(pk=pk)
            serializer = self.serializer_class(booking)
            return Response(serializer.data)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def patch(self, request, pk):
        try:
            booking = Booking.objects.get(pk=pk)
            serializer = self.serializer_class(booking, data=request.data,partial=True)
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
            Booking.objects.get(pk=pk).delete()
            return Response({"detail":"booking deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ve:
            raise ve
        except Exception as e:  # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#RestFramework Modules
from rest_framework import serializers

#project modules
from apps.booking.models import Event
from apps.booking.models import Booking

class EventSerializer(serializers.ModelSerializer):
    class meta:
        model = Event
        fields =['event_name','event_date' ,'location',#'capasity' 
                 ]
        
        
class BookingSerializer(serializers.ModelSerializer):
    class meta:
        model = Booking
        fields =['name','email','ph_no','event','booked_at']
    
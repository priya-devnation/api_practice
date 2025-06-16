#RestFramework Modules
from rest_framework import serializers



#project modules

from apps.booking.models import Booking


       
class BookingSerializer(serializers.ModelSerializer):
    class meta:
        model = Booking
        fields =['name','email','ph_no','event','booked_at']


    def validate_email(self, data):
        email = data.get('email')
        if email:
            existing_count = Booking.objects.filter(email=email).count()
            if not self.instance or self.instance.email  != email:
                if existing_count > 2:
                    raise serializers.ValidationError("Only 2 bookings are allowed for one email id.")
                return data


    def validate_booking_date(self, value):
        event = value.get('event_data')
        booking_date = value.get('booked_at')
        
        if event and booking_date:
            if booking_date >= event.date:
                raise serializers.ValidationError("Booking date must be before the event date.")
        
        return value
    
    

    
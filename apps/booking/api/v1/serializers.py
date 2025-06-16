#RestFramework Modules
from rest_framework import serializers

from time import timezone

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
        if value < timezone.now().event_date():
            raise serializers.ValidationError("Booking date cannot be in the past! ")
        return value 

    
#RestFramework Modules
from rest_framework import serializers




#project modules

from apps.booking.models import Booking


       
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields =['name','email','ph_no','event','booked_at']


    def validate(self, attrs):
        email = attrs.get('email')
        event = attrs.get('event')
        booked_at = attrs.get('booked_at')

        if email:
            existing_count = Booking.objects.filter(email=email).count()
            if self.instance is None or  self.instance.email  != email:
                if existing_count > 2:
                    raise serializers.ValidationError({"email" : "Only 2 bookings are allowed for one email id."})
                

        if event and booked_at and booked_at > event.event_date:
            raise serializers.ValidationError({"booked_at":"Booking date must be besfore the event date."})
        
        return attrs
    

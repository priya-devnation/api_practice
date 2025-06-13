# Restframework modules
from rest_framework import serializers

# Project modules
from apps.holiday.models import HolidayMaster

# Django modules
from django.utils import timezone


# Serializer for CurrencyMaster model

class HolidayMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidayMaster
        fields = ['id', 'label', 'start_datetime', 'end_datetime']

    def validate(self, value):
        start_datetime = value.get('start_datetime')
        end_datetime = value.get('end_datetime')
        if start_datetime and end_datetime and start_datetime >= end_datetime:
            raise serializers.ValidationError("start_datetime must be less than end_datetime.")
        if start_datetime:
            if start_datetime < timezone.now():
                raise serializers.ValidationError("start datetime cannot be in the past.")
        return value
    
    
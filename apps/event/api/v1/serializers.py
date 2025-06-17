#RestFramework Modules
from rest_framework import serializers


#project modules
from apps.event.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields =['event_name','event_date' ,'location','capacity']

    


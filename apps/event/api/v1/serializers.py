#RestFramework Modules
from rest_framework import serializers
from django.core.exceptions import ValidationError


#project modules
from apps.event.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields =['id','event_name','event_date' ,'location','capacity']

        

        


        


    


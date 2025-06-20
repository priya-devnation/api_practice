#from django modules
from django.db import models


# Project modules
from apps.event.models import Event
from utils.validators import phone_validator
#from apps.event.models import EventMaster

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    ph_no = models.CharField(max_length=15, validators=[phone_validator])
    event = models.ForeignKey(Event, on_delete = models.PROTECT, null=False, blank=False, related_name='booking_master_event_foriegn_key')  #foriegn key
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
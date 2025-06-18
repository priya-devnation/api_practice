#from django modules
from django.db import models

# Project modules
from apps.event.models import Event

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    ph_no = models.IntegerField(null=False, blank=False)
    event = models.ForeignKey(Event, on_delete = models.PROTECT)             #foriegn key
    booked_at = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.name
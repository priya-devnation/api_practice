#from django modules
from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100, null=False, blank=False)
    event_date = models.DateField(auto_now=True)
    location = models.CharField(max_length=100, null=False, blank=False)
    #location = models.LocationField(based_field=[], zoom=7, default= point(1.0,1.0))
    #capacity = models.IntegerField(max_value=5, null=False, blank=False)

    def ___str___(self):
        return self.event_name


class Booking(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    ph_no = models.IntegerField(max_length=10, null=False, blank=False)
    event = models.CharField(max_length=100, null=False, blank=False)
    booked_at = models.DateTimeField(auto_now_add=True)

    def ___str___(self):
        return self.name
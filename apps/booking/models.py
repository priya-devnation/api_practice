#from django modules
from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    ph_no = models.IntegerField(max_length=10, null=False, blank=False)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)             #foriegn key
    booked_at = models.DateTimeField(auto_now_add=True)

    def ___str___(self):
        return self.name
from django.db import models

        
# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100, null=False, blank=False)
    event_date = models.DateField(auto_now=True)
    location = models.CharField(max_length=100, null=False, blank=False)
    capacity = models.PositiveBigIntegerField(null=True,blank=True)

    def __str__(self):
        return self.event_name

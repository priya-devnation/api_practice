from django.db import models
from django.core.validators import MaxValueValidator


        
# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100, null=False, blank=False)
    event_date = models.DateField()
    location = models.CharField(max_length=100, null=False, blank=False)
    capacity = models.PositiveBigIntegerField(validators=[MaxValueValidator(5, message="capacity must be 5 or less.")],null=True,blank=True)

    def __str__(self):
        return self.event_name
    
    

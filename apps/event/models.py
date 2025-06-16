from django.db import models
from django.core.exceptions import ValidationError


def validate_capacity(value):
        if not value.isdigit():
            raise ValidationError("capacity must be a number")
        num = int(value)
        if num<1 or num>5:
            raise ValidationError("capacity must be in between 1 to 5.")
        
# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100, null=False, blank=False)
    event_date = models.DateField(auto_now=True)
    location = models.CharField(max_length=100, null=False, blank=False)
    capacity = models.CharField(max_length=2,
                                validators=[validate_capacity],
                                help_text="enter a number from 1 to 5" 
                            )
    def ___str___(self):
        return self.event_name

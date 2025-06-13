# Django modules
from django.db import models

class HolidayMaster(models.Model):
    label = models.CharField(max_length=100, null=False, blank=False)
    start_datetime = models.DateTimeField(null=False, blank=False, unique=True)
    end_datetime = models.DateTimeField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.label

#django modules
from django.contrib import admin

#project modules
from .models import Booking
from .models import Event

# Register your models here.
admin.site.register(Booking)
admin.site.register(Event)

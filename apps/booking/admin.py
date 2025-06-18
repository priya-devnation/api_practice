#django modules
from django.contrib import admin

#project modules
from .models import Booking


# Register your models here.
admin.site.register(Booking)


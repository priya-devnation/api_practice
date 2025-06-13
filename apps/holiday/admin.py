# Django modules
from django.contrib import admin

# Project modules
from apps.holiday.models import HolidayMaster

admin.site.register(HolidayMaster)
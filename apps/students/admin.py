# Django modules
from django.contrib import admin

# Project modules
from .models import Student

# Register your models here.

admin.site.register(Student)

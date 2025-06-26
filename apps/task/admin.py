from django.contrib import admin

#project Modules
from .models import Task

# Register your models here.
admin.site.register(Task)
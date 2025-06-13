from django.contrib import admin

#project modules
from .models import Todo

# Register your models here.
admin.site.register(Todo)

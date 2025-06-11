# Django modules
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)
    email = models.EmailField(unique=True,null=False, blank=False)
    course = models.CharField(max_length=100,null=False, blank=False)
    marks = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name

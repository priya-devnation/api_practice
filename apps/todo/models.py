# Django modules
from django.db import models

# Python modules
import uuid

# Create your models here.
class Todo(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True,unique=True)
    title = models.CharField(max_length=100,null=False,blank=False)
    description = models.CharField(max_length=100,null=False,blank=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

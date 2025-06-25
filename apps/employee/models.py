from django.db import models


# Python modules
import uuid

# Create your models here.
class Employee(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True,unique=True)
    Employee_name = models.CharField(max_length=100,null=False, blank=False)
    Employee_role = models.CharField(max_length=100,null=False, blank=False)

    def __str__(self):
        return self.Employee_name
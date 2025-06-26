from django.db import models
#from apps.employee.models import Employee

# Python modules
import uuid

# Create your models here.
class Task(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True,unique=True)
    Task_name = models.CharField(max_length=100,null=False, blank=False)
    Task_description = models.CharField(max_length=100,null=False, blank=False)
    Task_status = models.CharField(max_length=100,null=False, blank=False)
    Due_date = models.DateField(null=False, blank=False)
    #Employee_name = models.ForeignKey(Employee_name, on_delete = models.PROTECT, null=False, blank=False, related_name='task_master_employee_name_foriegn_key')  #foriegn key


    def __str__(self):
        return self.Task_name

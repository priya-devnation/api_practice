from django.db import models

from apps.employee.models import Employee

# Python modules
import uuid

# Create your models here.
class Task(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True,unique=True)
    task_name = models.CharField(max_length=100,null=False, blank=False)
    task_description = models.CharField(max_length=100,null=False, blank=False)
    task_status = models.CharField(max_length=15, choices=[('Todo', 'Todo'), ('In_progress', 'In_progress'),('Review', 'Review'),('Complete','complete')], default='Todo') # Buffer time type field for the service
    due_date = models.DateField(null=False, blank=False)
    employee_name = models.ForeignKey(Employee, on_delete = models.PROTECT, null=False, blank=False, related_name='task_master_employee_name_foriegn_key')  #foriegn key
    tags = models.CharField(max_length=15, choices=[('Internal', 'Internal'), ('HR', 'HR'),('Back_end', 'Back_end'),('Front_end','Front_end')], default='Internal')
    priority = models.CharField(max_length=10, choices=[('Urgent','Urgent'),('High','High'),('Normal','Normal'),('Low',('Low'))],default='Normal')

    def __str__(self):
        return self.task_name
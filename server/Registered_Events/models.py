from django.db import models
from django.utils import timezone


class Registered_Events(models.Model):
    Emp_id = models.CharField(max_length=50,default=' ')
    Event_id = models.CharField(max_length=50,default=' ')
    Employee_Registered_on = models.DateTimeField(default=timezone.now)

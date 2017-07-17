from django.db import models
from django.utils import timezone

class Employee(models.Model):
    Empfirst_name = models.CharField(max_length=100)
    Emplast_name = models.CharField(max_length=100)
    Emp_des = models.CharField(max_length=100)
    hired_date = models.DateTimeField(default=timezone.now)

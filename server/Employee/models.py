from django.db import models
from django.utils import timezone

class Employee(models.Model):
    #Emp_id = models.CharField(default=' ',max_length=50)#primary_key=True)
    Empfirst_name = models.CharField(max_length=100)
    Emplast_name = models.CharField(max_length=100)
    Emp_des = models.CharField(max_length=100)
    hired_date = models.DateTimeField(default=timezone.now)

    #def __str__(self):
    #    return "%s" % self.Emp_des

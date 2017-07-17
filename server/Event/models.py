from django.db import models
from django.utils import timezone

class Event(models.Model):
    Event_name = models.CharField(max_length=100)
    Event_description = models.CharField(max_length=100)
    Date_of_registration = models.DateTimeField(default=timezone.now)
    Date_of_Event = models.DateTimeField(default=timezone.now)
    Lastdate_of_registration = models.DateTimeField(default=Date_of_Event)

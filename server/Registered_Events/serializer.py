from rest_framework import serializers
from Registered_Events.models import Registered_Events

class Registered_Events_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Registered_Events
        fields = ("Emp_id","Event_id","Date_of_Event")

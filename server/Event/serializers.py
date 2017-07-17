from rest_framework import serializers
from Event.models import Event

class EventSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = Event
        fields = ("Event_name", "Event_description","Date_of_registration","Date_of_Event", "Lastdate_of_registration")

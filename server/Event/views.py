from django.shortcuts import render
from rest_framework import viewsets
from Event.models import Event
from Event.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

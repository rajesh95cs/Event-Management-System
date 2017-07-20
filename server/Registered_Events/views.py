from django.shortcuts import render
from rest_framework import viewsets
from Registered_Events.models import Registered_Events
from Registered_Events.serializer import Registered_Events_Serializer

class Registered_Events_Viewset(viewsets.ModelViewSet):

    queryset = Registered_Events.objects.all()
    serializer_class = Registered_Events_Serializer


# Create your views here.

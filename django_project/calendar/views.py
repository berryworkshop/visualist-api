from django.shortcuts import render
from .models import Event
from rest_framework import viewsets
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Events to be viewed or edited.
    '''
    queryset = Event.objects.all()
    serializer_class = EventSerializer

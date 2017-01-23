# from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from .models import Event, Place

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import (
    UserSerializer,
    GroupSerializer,
    EventSerializer,
    PlaceSerializer
)


class HomeView(TemplateView):
    template_name = 'visualist/home/home.html'


class SearchView(TemplateView):
    template_name = 'visualist/search/search.html'


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class EventView(DetailView):
    model = Event
    template_name = 'visualist/event/event.html'
    

class EventsView(ListView):
    model = Event
    template_name = 'visualist/events/events.html'


class EventViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Events to be viewed or edited.
    '''
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# class PlaceView(DetailView):
#     model = Place
#     template_name = 'visualist/place/place.html'
    

# class PlacesView(ListView):
#     model = Place
#     template_name = 'visualist/places/places.html'


class PlaceViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Places to be viewed or edited.
    '''
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

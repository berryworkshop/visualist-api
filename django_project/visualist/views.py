# from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from .models.time import Event

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, EventSerializer


class HomeView(TemplateView):
    template_name = 'visualist/home/home.html'


class SearchView(TemplateView):
    template_name = 'visualist/search/search.html'


# class PersonView(DetailView):
#     model = Person
#     template_name = 'visualist/person/person.html'


# class PeopleView(ListView):
#     model = Person
#     template_name = 'visualist/people/people.html'




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

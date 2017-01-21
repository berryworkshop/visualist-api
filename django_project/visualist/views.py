from .serializers import EventSerializer
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from rest_framework import viewsets
from .models.time import Event

class HomeView(TemplateView):
    template_name = 'visualist/home/home.html'


class SearchView(TemplateView):
    template_name = 'visualist/search/search.html'


class EventView(DetailView):
    model = Event
    template_name = 'visualist/event/event.html'
    

class EventsView(ListView):
    model = Event
    template_name = 'visualist/events/events.html'


# class PersonView(DetailView):
#     model = Person
#     template_name = 'visualist/person/person.html'


# class PeopleView(ListView):
#     model = Person
#     template_name = 'visualist/people/people.html'


class EventViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Events to be viewed or edited.
    '''
    queryset = Event.objects.all()
    serializer_class = EventSerializer

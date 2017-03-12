# from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from .models import Event, Place, Work, Body

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import (
    UserSerializer,
    GroupSerializer,
    EventSerializer,
    VenueSerializer,
    WorkSerializer,
    PersonSerializer,
    OrganizationSerializer,
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


# class VenueView(DetailView):
#     model = Venue
#     template_name = 'visualist/place/place.html'
    

# class VenuesView(ListView):
#     model = Venue
#     template_name = 'visualist/places/places.html'


class VenueViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Views to be viewed or edited.
    '''
    queryset = Place.objects.all()
    serializer_class = VenueSerializer


# class WorkView(DetailView):
#     model = Work
#     template_name = 'visualist/work/work.html'
    

# class WorksView(ListView):
#     model = Work
#     template_name = 'visualist/works/works.html'


class WorkViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Views to be viewed or edited.
    '''
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


# class PersonView(DetailView):
#     model = Person
#     template_name = 'visualist/person/person.html'
    

# class PeopleView(ListView):
#     model = Person
#     template_name = 'visualist/people/people.html'


class PersonViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Views to be viewed or edited.
    '''
    queryset = Body.objects.filter(record_type='PERSON')
    serializer_class = PersonSerializer


# class OrganizationView(DetailView):
#     model = Organization
#     template_name = 'visualist/organization/organization.html'
    

# class OrganizationsView(ListView):
#     model = Organization
#     template_name = 'visualist/organization/organization.html'


class OrganizationViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Views to be viewed or edited.
    '''
    queryset = Body.objects.filter(record_type='ORGANIZATION')
    serializer_class = OrganizationSerializer

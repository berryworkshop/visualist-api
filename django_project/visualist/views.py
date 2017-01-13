from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from timeline.models import Event


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

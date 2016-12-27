from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from timeline.models import Event


class HomeView(TemplateView):
    template_name = 'visualist/home.html'


class EventView(DetailView):
    model = Event
    template_name = 'visualist/event.html'


class EventListView(ListView):
    model = Event
    template_name = 'visualist/event_list.html'
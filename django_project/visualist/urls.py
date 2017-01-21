from .views import EventViewSet, HomeView, SearchView, EventView, EventsView
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'events', EventViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^search$', SearchView.as_view(), name='search'),
    
    url(r'^events$', EventsView.as_view(), name='events'),
    url(r'^events/(?P<pk>[0-9]+)$', EventView.as_view(), name='event'),

    url(r'^django-admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
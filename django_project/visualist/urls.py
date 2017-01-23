from .views import (
    HomeView,
    SearchView,
    UserViewSet,
    GroupViewSet,
    EventView,
    EventsView,
    EventViewSet,
    # PlaceView,
    # PlacesView,
    PlaceViewSet,
)
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'events', EventViewSet)
router.register(r'places', PlaceViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^search$', SearchView.as_view(), name='search'),
    
    url(r'^events$', EventsView.as_view(), name='events'),
    url(r'^events/(?P<pk>[0-9]+)$', EventView.as_view(), name='event'),

    # url(r'^places$', PlacesView.as_view(), name='places'),
    # url(r'^places/(?P<pk>[0-9]+)$', PlaceView.as_view(), name='place'),

    url(r'^django-admin/', admin.site.urls),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

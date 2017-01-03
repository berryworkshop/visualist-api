from django.conf.urls import url, include
from django.contrib import admin
from .views import HomeView, EventView, EventListView, SpaView

from cms import urls as cms_urls
from timeline import urls as timeline_urls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    
    url(r'^events$', EventListView.as_view(), name='event_list'),
    url(r'^events/(?P<pk>[0-9]+)$', EventView.as_view(), name='event'),

    url(r'^cms/', include(cms_urls)),
    url(r'^timeline/', include(timeline_urls)),

    url(r'^django-admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

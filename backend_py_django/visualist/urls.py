from .views import (
    HomeView,
    SearchView,
    UserViewSet,
    GroupViewSet,
    EventView,
    EventsView,
    EventViewSet,
    # VenueView,
    # VenuesView,
    VenueViewSet,
    # WorkView,
    # WorksView,
    WorkViewSet,
    # PersonView,
    # PeopleView,
    PersonViewSet,
    # OrganizationView,
    # OrganizationsView,
    OrganizationViewSet,
)
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'events', EventViewSet)
router.register(r'venues', VenueViewSet)
router.register(r'works', WorkViewSet)
router.register(r'people', PersonViewSet, base_name='people')
router.register(r'orgs', OrganizationViewSet, base_name='organizations')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^search$', SearchView.as_view(), name='search'),
    
    url(r'^events$', EventsView.as_view(), name='events'),
    url(r'^events/(?P<pk>[0-9]+)$', EventView.as_view(), name='event'),

    # url(r'^venues$', VenuesView.as_view(), name='venues'),
    # url(r'^venues/(?P<pk>[0-9]+)$', VenueView.as_view(), name='venue'),

    # url(r'^works$', WorksView.as_view(), name='works'),
    # url(r'^works/(?P<pk>[0-9]+)$', WorkView.as_view(), name='work'),

    # url(r'^people$', PeopleView.as_view(), name='people'),
    # url(r'^people/(?P<pk>[0-9]+)$', PersonView.as_view(), name='person'),

    # url(r'^orgs$', OrganizationsView.as_view(), name='organizations'),
    # url(r'^orgs/(?P<pk>[0-9]+)$',
        # OrganizationView.as_view(), name='organization'),

    url(r'^django-admin/', admin.site.urls),

    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-token-auth-jwt/', obtain_jwt_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


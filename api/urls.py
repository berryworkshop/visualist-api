from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import (
    UserViewSet,
    GroupViewSet,
    RecordViewSet,
    EventViewSet,
    EntityViewSet,
    RelationViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'records', RecordViewSet)
router.register(r'events', EventViewSet)
router.register(r'entities', EntityViewSet)
router.register(r'relations', RelationViewSet)

urlpatterns = [
    # url(r'^$', views.base_view),
    url(r'^auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token-auth', obtain_jwt_token),
    url(r'^token-refresh', refresh_jwt_token),
    url(r'^', include(router.urls)),
]

from django.conf.urls import url, include
from rest_framework import routers, renderers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    UserViewSet,
    GroupViewSet,
    RecordViewSet,
    EntityList,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'records', RecordViewSet)

urlpatterns = [
    # url(r'^$', views.base_view),
    url(r'^auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token-auth', obtain_jwt_token),
    url(r'^token-refresh', refresh_jwt_token),

    url(r'^entities', EntityList.as_view(), name='entity-list'),

    url(r'^', include(router.urls)),

]

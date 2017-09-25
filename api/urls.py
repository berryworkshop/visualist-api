from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'records', views.RecordViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'entities', views.EntityViewSet)

urlpatterns = [
    # url(r'^$', views.base_view),
    url(r'^auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token-auth', obtain_jwt_token),
    url(r'^token-refresh', refresh_jwt_token),
    url(r'^', include(router.urls)),
]

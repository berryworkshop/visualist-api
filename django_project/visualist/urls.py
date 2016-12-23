from django.conf.urls import url, include
from django.contrib import admin
from .views import HomeView
from cms import urls as cms_urls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),



    url(r'^cms/', include(cms_urls)),

    url(r'^django-admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from django.conf.urls import include, url
from django.contrib import admin
import api.urls as api_urls
from .views import AppView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),

    # client urls
    url(r'^calendar', AppView.as_view(), name='calendar'),
    url(r'^directory', AppView.as_view(), name='directory'),
    url(r'^map', AppView.as_view(), name='map'),
    url(r'^search', AppView.as_view(), name='search'),
    url(r'^user', AppView.as_view(), name='user'),
    url(r'^$', AppView.as_view(), name='home'),
]

from django.conf.urls import include, url
from django.contrib import admin
import api.urls as api_urls
from .views import AppView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
    url(r'^$', AppView.as_view(), name='app'),
]

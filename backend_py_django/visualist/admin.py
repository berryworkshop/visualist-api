from django.contrib import admin
from .models import (Event, Place, Work, Body)


admin.site.register(Event)
admin.site.register(Place)
admin.site.register(Work)
admin.site.register(Body)
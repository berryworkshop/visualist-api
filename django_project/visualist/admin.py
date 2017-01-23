from django.contrib import admin
from .models import (Event, Venue, Work, Contact)


admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Work)
admin.site.register(Contact)
from django.contrib import admin
from .models import (
    Period, Event, Moment)

# Register your models here.
admin.site.register(Period)
admin.site.register(Event)
admin.site.register(Moment)

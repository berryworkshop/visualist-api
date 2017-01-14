from django.contrib import admin
from .models import (
    Event,
    # Period,
    )


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


# admin.site.register(Period)
admin.site.register(Event, EventAdmin)
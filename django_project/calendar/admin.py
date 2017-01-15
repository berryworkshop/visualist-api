from django.contrib import admin
from .models import (
    Event,
    )


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Event, EventAdmin)
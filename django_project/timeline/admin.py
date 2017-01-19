from django.contrib import admin
from .models import (
    Event,
    )
from base.admin import (
    WorkEventInline,
    EventVenueInline,
    EventContactInline
)


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = (
        WorkEventInline,
        EventVenueInline,
        EventContactInline,
    )


admin.site.register(Event, EventAdmin)
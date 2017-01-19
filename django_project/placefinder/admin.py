from django.contrib import admin
from .models import (
    Address,
    HourSet,
    Place,
    Venue,
)
from base.admin import (
    WorkVenueInline,
    EventVenueInline,
    ContactVenueInline
)

class VenueAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = (
        WorkVenueInline,
        EventVenueInline,
        ContactVenueInline,
    )


admin.site.register(Address)
admin.site.register(HourSet)
admin.site.register(Place)
admin.site.register(Venue, VenueAdmin)
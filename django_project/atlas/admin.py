from django.contrib import admin
from .models import (
    Address,
    HourSet,
    Place,
    Venue,
    )


class VenueAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Address)
admin.site.register(HourSet)
admin.site.register(Place)
admin.site.register(Venue, VenueAdmin)
from django.contrib import admin
from .models import (
    Venue,
    )


class VenueAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Venue, VenueAdmin)
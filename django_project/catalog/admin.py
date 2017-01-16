from django.contrib import admin
from .models import (
    # Work,
    PhysicalWork,
    TemporalWork,
    DimensionSet,
    )


class PhysicalWorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class TemporalWorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


# admin.site.register(Work, WorkAdmin)
admin.site.register(PhysicalWork, PhysicalWorkAdmin)
admin.site.register(TemporalWork, TemporalWorkAdmin)
admin.site.register(DimensionSet)
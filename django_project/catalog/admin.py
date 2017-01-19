from django.contrib import admin
from .models import (
    Work,
    DimensionSet,
    )
from base.admin import (
    WorkContactInline,
    WorkEventInline,
    WorkVenueInline
)


class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = (
        WorkContactInline,
        WorkEventInline,
        WorkVenueInline,
    )


# admin.site.register(Work, WorkAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(DimensionSet)
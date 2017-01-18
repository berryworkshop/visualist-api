from django.contrib import admin
from .models import (
    Work,
    DimensionSet,
    )


class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


# admin.site.register(Work, WorkAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(DimensionSet)
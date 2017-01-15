from django.contrib import admin
from .models import (
    Work,
    )


class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Work, WorkAdmin)
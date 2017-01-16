from django.contrib import admin
from .models import (
    Page,
    )

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Page)

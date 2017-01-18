from django.contrib import admin
from .models import (
    Contact,
    Alias,
    Account,
    Email,
    Phone,
    Website,
    )


class ContactAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Contact, ContactAdmin)
admin.site.register(Alias)
admin.site.register(Account)
admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Website)

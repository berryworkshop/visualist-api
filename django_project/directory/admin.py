from django.contrib import admin
from .models import (
    # Contact,
    Person,
    Organization,
    Alias,
    Account,
    Email,
    Phone,
    Website,
    )


class OrganizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("last_name", "first_name")}


admin.site.register(Person, PersonAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Alias)
admin.site.register(Account)
admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Website)

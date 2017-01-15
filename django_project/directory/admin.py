from django.contrib import admin
from .models import (
    Account,
    # Contact,
    Email,
    # HourSet,
    Organization,
    Person,
    Phone,
    Website,
    )


class OrganizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("last_name", "first_name")}


admin.site.register(Account)
# admin.site.register(Contact)
admin.site.register(Email)
# admin.site.register(HourSet)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Phone)
admin.site.register(Website)

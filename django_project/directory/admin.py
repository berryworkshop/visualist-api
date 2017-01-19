from django.contrib import admin
from .models import (
    Contact,
    Relationship,
    # Alias,
    # Account,
    # Email,
    # Phone,
    # Website,
)
from base.admin import (
    WorkContactInline,
    EventContactInline,
    ContactVenueInline
)


class ParentChildInline(admin.StackedInline):
    model = Relationship
    fk_name = 'child'
    extra = 1


class ChildParentInline(admin.StackedInline):
    model = Relationship
    fk_name = 'parent'
    extra = 1


class ContactAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = (
        ParentChildInline,
        ChildParentInline,
        WorkContactInline,
        EventContactInline,
        ContactVenueInline,
    )


admin.site.register(Contact, ContactAdmin)
# admin.site.register(Alias)
# admin.site.register(Account)
# admin.site.register(Email)
# admin.site.register(Phone)
# admin.site.register(Website)

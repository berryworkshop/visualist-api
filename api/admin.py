from django.contrib import admin
from api.models import (
    Image,
    Record,
    Relation,
    Term,
    Date,
    Location,
    Source,
)

class RecordAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class RelationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("value",)}

class TermAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("vocabulary", "value",)}


admin.site.register(Image)
admin.site.register(Record, RecordAdmin)
admin.site.register(Relation)
admin.site.register(Term, TermAdmin)
admin.site.register(Date)
admin.site.register(Location)
admin.site.register(Source)

from django.contrib import admin
from api.models import (
    Image,
    Record,
    Relation,
    Term,
    Date,
    Location,
    Source,
    Snippet,
)

class RecordAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('label', 'terms', 'is_primary')
    search_fields = ('name',
    # 'properties'
    )

class RelationAdmin(admin.ModelAdmin):
    list_filter = ('predicate',)
    search_fields = ('subject__name', 'predicate', 'dobject__name',
    # 'properties',
    )

class TermAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("vocabulary", "value",)}


admin.site.register(Image)
admin.site.register(Record, RecordAdmin)
admin.site.register(Relation, RelationAdmin)
admin.site.register(Term, TermAdmin)
admin.site.register(Date)
admin.site.register(Location)
admin.site.register(Source)
admin.site.register(Snippet)

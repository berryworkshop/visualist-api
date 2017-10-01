from django.contrib import admin
from api.models import (
    Image,
    Record,
    Relation,
    Term,
)

admin.site.register(Image)
admin.site.register(Record)
admin.site.register(Relation)
admin.site.register(Term)

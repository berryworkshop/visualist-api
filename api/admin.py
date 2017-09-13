from django.contrib import admin
from api.models import (
    Address,
    Email,
    Identifier,
    Image,
    License,
    Phone,
    Record,
    Relation,
    Resource,
    SocialAccount,
    Tag,
    Term,
)

admin.site.register(Address)
admin.site.register(Email)
admin.site.register(Identifier)
admin.site.register(Image)
admin.site.register(License)
admin.site.register(Phone)
admin.site.register(Record)
admin.site.register(Relation)
admin.site.register(Resource)
admin.site.register(SocialAccount)
admin.site.register(Tag)
admin.site.register(Term)

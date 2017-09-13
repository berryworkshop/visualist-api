from django.contrib import admin
from api.models import (
    Address,
    Term,
    # Collection,
    Email,
    # Event,
    Identifier,
    Image,
    # Organization,
    # Page,
    # Person,
    Phone,
    # Place,
    # Post,
    # Snippet,
    SocialAccount,
    Tag,
    # Work,
    Record,
    Relation,
)

admin.site.register(Address)
admin.site.register(Term)
# admin.site.register(Collection)
admin.site.register(Email)
# admin.site.register(Event)
admin.site.register(Identifier)
admin.site.register(Image)
# admin.site.register(Organization)
# admin.site.register(Page)
# admin.site.register(Person)
admin.site.register(Phone)
# admin.site.register(Place)
# admin.site.register(Post)
# admin.site.register(Snippet)
admin.site.register(SocialAccount)
admin.site.register(Tag)
admin.site.register(Record)
admin.site.register(Relation)
# admin.site.register(Work)

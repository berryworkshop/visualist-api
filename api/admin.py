from django.contrib import admin
from api.models import (
    Resource, License, Snippet, Event, Work, Person, Organization,
    Place, Post, Page, Collection, Image, Address, Phone, Email, SocialAccount,
    Category, Tag, Identifier, Nationality
)

admin.site.register(Resource)
admin.site.register(License)
admin.site.register(Snippet)
admin.site.register(Image)
admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(SocialAccount)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Identifier)
admin.site.register(Nationality)
admin.site.register(Event)
admin.site.register(Work)
admin.site.register(Person)
admin.site.register(Organization)
admin.site.register(Place)
admin.site.register(Post)
admin.site.register(Page)
admin.site.register(Collection)

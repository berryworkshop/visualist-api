from django.contrib import admin
from .models import (
    WorkContactJoin,
    WorkEventJoin,
    WorkVenueJoin,
    EventVenueJoin,
    EventContactJoin,
    ContactVenueJoin,
)


class WorkContactInline(admin.StackedInline):
    model = WorkContactJoin
    extra = 1
    # raw_id_fields = ("work", "contact")
    search_fields = ['work__name', 'contact__name']


class WorkEventInline(admin.StackedInline):
    model = WorkEventJoin
    extra = 1


class WorkVenueInline(admin.StackedInline):
    model = WorkVenueJoin
    extra = 1


class EventVenueInline(admin.StackedInline):
    model = EventVenueJoin
    extra = 1


class EventContactInline(admin.StackedInline):
    model = EventContactJoin
    extra = 1


class ContactVenueInline(admin.StackedInline):
    model = ContactVenueJoin
    extra = 1

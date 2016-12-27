from django.db import models
from django.urls import reverse
from cms.models import Record, Term


class Moment(Record):
    '''
    A named point in time.
    '''

    name = models.CharField(blank=False, null=False, max_length=255)

    def __str__(self):
        return self.name


class Event(Moment):
    '''An art event, performance or happening.'''

    TYPES = [
        "event",
        "performance",
    ]

    def get_absolute_url(self):
        return reverse('event', args=[self.pk])


class Period(Term):
    '''
    A named span of time, e.g. an epock, era, or an art historical movement.
    '''
    pass
from django.db import models
from cms.models import Record, Term


class Moment(Record):
    '''
    A named point in time.
    '''
    pass


class Event(Moment):
    '''An art event, performance or happening.'''
    pass

    TYPES = [
        "event",
        "performance"
    ]


class Period(Term):
    '''
    A named span of time, e.g. an epock, era, or an art historical movement.
    '''
    pass
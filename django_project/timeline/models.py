from django.db import models
from cms.models import Record, Term


class Period(Term):
    '''Period'''
    pass


class Event(Record):
    '''Event'''
    pass


class Exhibit(Event):
    '''Exhibit'''
    pass


class Performance(Event):
    '''Performance'''
    pass


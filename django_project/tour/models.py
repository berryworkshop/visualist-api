from django.db import models
from cms.models import Record, Term


class Place(Record):
    '''A named point in space.'''
    pass


class Venue(Place):
    '''A venue for showing or experiencing art.'''
    pass


class Space(Term):
    '''A named two-dimensional area, with many points, of arbitrary shape.'''
    pass


class State(Space):
    '''A US State.'''
    pass


class City(Space):
    '''A city, town or village.'''
    pass


class Neighborhood(Space):
    '''A neighborhood or community area, officially recognized or not.'''
    pass


class PostalCode(Space):
    '''A postal code, e.g. a US Zip Code.'''
    pass


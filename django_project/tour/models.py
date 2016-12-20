from django.db import models
from cms.models import Record


class Place(Record):
    '''Place'''
    pass


class Space(Place):
    '''Space'''
    pass


class State(Space):
    '''State'''
    pass


class City(Space):
    '''City'''
    pass


class Neighborhood(Space):
    '''Neighborhood'''
    pass


class District(Space):
    '''District'''
    pass


class Zipcode(Space):
    '''Zipcode'''
    pass


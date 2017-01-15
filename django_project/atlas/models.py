from django.db import models
from base.models import Record
# from thesaurus.models import Term


class PointInSpace(Record):
    '''
    A spot on a map.
    Not generally to be used directly.  Should not have a view, for example.
    This uses multi-table inheritance, so be careful with adjustments.
    The abstract superclass for Venues, or other relevant future Record types.
    '''
    pass


class Venue(PointInSpace):
    '''A named venue for showing or experiencing art.'''
    
    name = models.CharField(max_length=255)
    # capacity


# class Area(Term):
#     '''A named two-dimensional area, with many points, of arbitrary shape.'''
#     pass


# class State(Area):
#     '''A US State.'''
#     pass


# class City(Area):
#     '''A city, town or village.'''
#     pass


# class Neighborhood(Area):
#     '''A neighborhood or community area, officially recognized or not.'''
#     pass
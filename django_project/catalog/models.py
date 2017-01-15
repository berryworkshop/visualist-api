from django.db import models
from base.models import Base, Record
from thesaurus.models import Term



class Thing(Record):
    '''
    A physical object, without the characteristics of anartwork,
    e.g. an ephemeron or natural structure.
    This uses multi-table inheritance, so be careful with adjustments.
    The abstract superclass for Works, or other relevant future Record types.
    Not generally to be used directly.  Should not have a view, for example.
    '''
    pass


class Work(Thing):
    '''
    Usually a piece of artwork, a Work is the primary unit used.
    '''
    pass

    CONDITIONS = [
        'mint',
        'excellent', 
        'very good',
        'good',
        'fair',
        'poor',
    ]

class Dimension(Base):
    '''Length, width, height, or duration.'''
    pass

    TYPES = [
        'length',
        'width', 
        'height', 
        'duration',
    ]


# class Medium(Term):
#     '''The materials, tools or techniques used to make the work.'''
#     pass


# class Genre(Term):
#     '''
#     A formal art historical classification.
#     '''
#     pass
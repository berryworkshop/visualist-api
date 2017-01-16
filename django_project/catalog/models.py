from django.db import models
from base.models import Base, Record
from thesaurus.models import Term
from directory.models import Contact
from atlas.models import Venue


class Thing(Record):
    '''
    A physical object, without the characteristics of an artwork,
    e.g. an ephemeron or natural structure.
    '''
    
    name = models.CharField(max_length=100)
    synopsis = models.TextField(max_length=250, blank=True, null=True)
    dimension_set = models.ForeignKey('DimensionSet', blank=True, null=True)

    location = models.ForeignKey(Venue, on_delete=models.PROTECT)


class Work(Thing):
    '''
    Usually a piece of artwork, a Work is the primary unit used.
    '''
    
    creators = models.ManyToManyField(Contact)

    # Medium
    # Genre
    # Condition


# class Ephemeron(Thing):
#     '''
#     A thing associated with an Event or Work.
#     '''
#     pass


class DimensionSet(Base):
    '''A set of dimensions for '''

    UNITS = (
        ('mm', 'millimeters'),
        ('cm', 'centimeters'),
        ('m',  'meters'),
        ('in', 'inches'),
        ('ft', 'feet'),
    )
    
    length = models.DecimalField(max_digits=7, decimal_places=3)
    width  = models.DecimalField(max_digits=7, decimal_places=3)
    height = models.DecimalField(max_digits=7, decimal_places=3,
        blank=True, null=True)
    dimension_unit = models.CharField(max_length=2,
        choices=UNITS, default='in')


# class Medium(Term):
#     '''The materials, tools or techniques used to make the work.'''
#     pass


# class Genre(Term):
#     '''
#     A formal art historical classification.
#     '''
#     pass

# class Condition(Term):
#     '''
#     What shape is this thing in.
#     '''
#
#     CONDITIONS = [
#         'mint',
#         'excellent', 
#         'very good',
#         'good',
#         'fair',
#         'poor',
#     ]
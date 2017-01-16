from django.db import models
from base.models import Base, Record
from thesaurus.models import Term
from directory.models import Contact
from atlas.models import Venue


class Work(Record):
    '''
    A thing created by a human or humans.
    '''
    
    name = models.CharField(max_length=100, default="Untitled")
    synopsis = models.TextField(max_length=250, blank=True)
    creators = models.ManyToManyField(Contact, blank=True)


class PhysicalWork(Work):
    '''
    A physical work, with mass and volume.
    '''

    location = models.ForeignKey(Venue, on_delete=models.PROTECT,
        blank=True, null=True)   
    dimension_set = models.ForeignKey('DimensionSet', blank=True, null=True) 

    # Medium
    # Genre
    # Condition


class TemporalWork(Work):
    '''A performable, time-driven work.'''

    pass
    # duration = models.DecimalField(max_digits=, decimal_places=2)


# class Ephemeron(Work):
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

    def __str__(self):
        return "{}x{}x{} {}".format(
            self.length, self.width, self.height, self.dimension_unit)


# class Medium(Term):
#     '''The materials, tools or techniques of which the work consists.'''
#     pass


# class Format(Term):
#     '''The materials, tools or techniques on which the work relies.'''
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
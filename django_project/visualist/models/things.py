from django.db import models
from base.models import Base, Record
# from thesaurus.models import Term
# from .people import Contact
# from .space import Venue
# from .time import Event
# from .joins import WorkEventJoin, WorkVenueJoin, WorkContactJoin


class Work(Record):
    '''
    A thing created by a human or humans.
    '''

    # for physical works
    dimension_set = models.ForeignKey('DimensionSet', blank=True, null=True) 

    events = models.ManyToManyField('Event', blank=True,
        through='WorkEventJoin')
    venues = models.ManyToManyField('Venue', blank=True,
        through='WorkVenueJoin')
    contacts = models.ManyToManyField('Contact', blank=True,
        through='WorkContactJoin')

    # for temporal works
    # duration = models.DecimalField(max_digits=, decimal_places=2)


# class Ephemeron(Record):
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
        return "{} x {} x {} {}".format(
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
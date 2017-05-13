from django.db import models
from .base import Base, Record
# from thesaurus.models import Term
# from .people import Body
# from .space import Place
# from .time import Event
# from .joins import WorkEventJoin, WorkPlaceJoin, WorkBodyJoin


class Work(Record):
    '''
    A thing created by a human or humans.
    '''

    #
    # Base fields
    # # #

    TYPES = (
        ('MATERIAL','material works, e.g. painting, sculpture'),
        ('TEMPORAL','temporal works, e.g. a performance')
    )
    record_type = models.CharField(max_length=20,
        choices=TYPES,
        default="MATERIAL")

    events = models.ManyToManyField('Event', blank=True,
        through='WorkEventJoin')
    places = models.ManyToManyField('Place', blank=True,
        through='WorkPlaceJoin')
    bodies = models.ManyToManyField('Body', blank=True,
        through='WorkBodyJoin')

    def __str__(self):
        return name

    def get_absolute_url(self):
        # TODO
        return '/'

    # 
    # Physical fields
    # # #

    dimension_set = models.ForeignKey('DimensionSet', blank=True, null=True) 

    # 
    # Temporal Fields
    # # #

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
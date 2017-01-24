from django.db import models
from .base import Base, Record
# from thesaurus.models import Term
# from .people import Body
# from .countries import COUNTRIES
from django.core.validators import MaxValueValidator, MinValueValidator


class Place(Record):
    '''
    A named place, usually a venue, for showing or experiencing art.
    '''

    #
    # Base fields
    # # #

    TYPES = (
        ('VENUE','venue'), # more later
    )
    record_type = models.CharField(max_length=20,
        choices=TYPES,
        default="VENUE")

    address = models.ForeignKey('Address', on_delete=models.PROTECT,
        blank=True, null=True)
    room = models.CharField(max_length=250, blank=True)
    
    latitude = models.DecimalField(
        max_digits=10, decimal_places=8,
        validators=[MaxValueValidator(90), MinValueValidator(-90)],
        null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=11, decimal_places=8,
        validators=[MaxValueValidator(180), MinValueValidator(-180)],
        null=True, blank=True)
    # altitude = models.DecimalField(
    #     max_digits=11, decimal_places=4,
    #     blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.occupant

    def get_absolute_url(self):
        # TODO
        return '/'

    def update_coordinates_from_address(self):
        # TODO
        pass

    def update_address_from_coordinates(self):
        # TODO
        pass


    #
    # Venue fields
    # # #

    hours_open = models.OneToOneField('HourSet', on_delete=models.PROTECT,
        blank=True, null=True)
    appointment_only = models.BooleanField(default=False)


class Address(Base):
    '''A street address.'''

    class Meta:
        verbose_name_plural = "addresses"

    street = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state_province = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=3,
        # choices=COUNTRIES,
        default="USA")

    def __str__(self):
        streets = [s.strip() for s in self.street.split('\n')]
        street = ', '.join(streets)
        return "{}, {}, {}, {}, {}".format(street, self.city,
            self.state_province, self.postal_code, self.country)


class HourSet(Base):
    '''A set of operating hours'''

    pass


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
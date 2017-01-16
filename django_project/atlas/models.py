from django.db import models
from base.models import Base, Record
# from thesaurus.models import Term
from directory.models import Contact
from .countries import COUNTRIES
from django.core.validators import MaxValueValidator, MinValueValidator

class Place(Base):
    '''
    An abstract unit of geographic space. 
    This uses multi-table inheritance, so be careful with adjustments.
    The abstract superclass for Events, or other relevant future Record types.
    Not generally to be used directly.  Should not have a view, for example.
    '''

    address = models.ForeignKey('Address', on_delete=models.PROTECT)
    room = models.CharField(max_length=250, blank=True, null=True)

    latitude = models.DecimalField(
        max_digits=10, decimal_places=8,
        validators=[MaxValueValidator(90), MinValueValidator(-90)])
    longitude = models.DecimalField(
        max_digits=11, decimal_places=8,
        validators=[MaxValueValidator(180), MinValueValidator(-180)])
    # altitude = models.DecimalField(
    #     max_digits=11, decimal_places=4,
    #     blank=True, null=True)

    def update_coordinates_from_address(self):
        # TODO
        pass

    def update_address_from_coordinates(self):
        # TODO
        pass

    def __str__(self):
        return "{}, {}".format(self.longitude, self.latitude)


class Venue(Record):
    '''A named venue for showing or experiencing art.'''
    
    name = models.CharField(max_length=100, blank=True, null=True)
    synopsis = models.TextField(max_length=250, blank=True, null=True)

    occupant = models.OneToOneField(Contact, on_delete=models.PROTECT)
    hours_open = models.OneToOneField('HourSet', on_delete=models.PROTECT)
    appointment_only = models.BooleanField(default=False)

    place = models.ForeignKey('Place',
        on_delete=models.PROTECT, blank=True, null=True)

    # capacity

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.occupant


class Address(Base):
    '''A street address.'''

    class Meta:
        verbose_name_plural = "addresses"

    street = models.TextField()
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=3,
        choices=COUNTRIES,
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
from django.db import models
from cms.models import Record, Base


class Entity(Record):
    '''
    Superclass to collect shared functionality between Person and Organization.
    '''

    class Meta:
        abstract = True
    pass


class Person(Entity):
    '''A human being.'''
    pass


class Organization(Entity):
    '''An organized group of humans.'''
    pass

    TYPES = [
        'school',
        'gallery', 
        'museum',
    ]


class ContactItem(Base):
    '''A superclass for shared functionality between contact line-items.'''

    class Meta:
        abstract = True

    TYPES = [
        'default',
        'work', 
        'personal',
    ]

    pass


class Account(ContactItem):
    '''A social media account'''
    pass


class Address(ContactItem):
    '''A street address.'''
    pass


class Email(ContactItem):
    '''An email address.'''
    pass


class Phone(ContactItem):
    '''A phone number.'''
    pass


class Website(ContactItem):
    '''The highest-level relevant website URL of a website.'''
    pass


class HourSet(Base):
    '''A defined set of operating hours.'''
    pass


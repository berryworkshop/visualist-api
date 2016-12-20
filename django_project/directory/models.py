from django.db import models
from cms.models import Record, Base


class Entity(Record):
    '''Entity'''
    pass


class Person(Entity):
    '''Person'''
    pass


class Organization(Entity):
    '''Organization'''
    pass


class School(Organization):
    '''School'''
    pass


class Gallery(Organization):
    '''Gallery'''
    pass


class Museum(Organization):
    '''Museum'''
    pass


class Venue(Organization):
    '''Venue'''
    pass


class ContactItem(Base):
    '''ContactItem'''
    pass


class Account(ContactItem):
    '''Account'''
    pass


class Address(ContactItem):
    '''Address'''
    pass


class Email(ContactItem):
    '''Email'''
    pass


class Phone(ContactItem):
    '''Phone'''
    pass


class Website(ContactItem):
    '''Website'''
    pass


class Hours(Base):
    '''Hours'''
    pass


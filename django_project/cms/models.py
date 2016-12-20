from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Base(models.Model):
    '''Base class as a foundation for most others.'''
    
    class Meta:
        abstract = True
    
    created = models.DateTimeField(default=now)
    modified = models.DateTimeField(auto_now=True)
    # created_by = User.???

    def get_absolute_url(self):
        return reverse('home')


class Log(Base):
    '''Misc. website logs, for blame, among other things.'''
    pass


class Announcement(Base):
    '''Announcement'''
    pass


#
# Records
#


class RecordSet(Base):
    '''RecordSet'''
    pass


class Record(Base):
    '''
    The central class for the Visualist system; the basic unit manipulated
    by the User in the interface.
    '''
    pass


class Page(Record):
    '''Page'''
    pass


class Article(Page):
    '''Article'''
    pass


class Link(Record):
    '''Link'''
    pass


class Relation(Base):
    '''Relation'''
    pass


#
# Field Tables
#

class Name(Base):
    '''Name'''
    pass


class Identifier(Base):
    '''Identifier'''
    pass


class Abstract(Base):
    '''Abstract'''
    pass


class Description(Base):
    '''Description'''
    pass


#
# Controlled Vocabulary
#

class Vocabulary(Base):
    '''Vocabulary'''
    pass


class Term(Base):
    '''Term'''
    pass


class Language(Term):
    '''Language'''
    pass


class Unit(Term):
    '''Unit'''
    pass


class Audience(Term):
    '''Audience'''
    pass


class Subject(Term):
    '''Subject'''
    pass


class License(Term):
    '''License'''
    pass


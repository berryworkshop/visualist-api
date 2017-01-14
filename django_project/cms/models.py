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


# class Log(Base):
#     '''Misc. website logs, for migrations, blame, among other things.'''
#     pass


#
# Records
#


class Record(Base):
    '''
    The central class for the Visualist system; the basic unit manipulated
    by the User in the interface.

    This is a very important class, and is used in other apps and classes.
    Manipulate with care.
    '''
    
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.slug


class Page(Record):
    '''
    A general-purpose, arbitrary website page, e.g. About, Copyright, etc.
    '''
    pass


# class Article(Page):
#     '''A Page with a listed author, post date, and other blog-like features.'''
#     pass


# class Link(Record):
#     '''A formal, named link, usually to an external resource on the web.'''
#     pass


# class RecordSet(Base):
#     '''A list of records for Users to share and save.'''
#     pass


# class Relation(Base):
#     '''
#     A connection to another local model, usually between Records
#     and their derivatives.
#     '''
#     pass


#
# Field Tables
#

# class Name(Base):
#     '''
#     A structured (additional) Name attribute, usable in multiple,
#     i.e. to simulate Dublin Core.  Usually from an external source.
#     '''
#     pass


# class Identifier(Base):
#     '''
#     A structured (additional) Identifier attribute, usable in multiple,
#     i.e. to simulate Dublin Core.  Usually from an external source.
#     '''
#     pass


# class Description(Base):
#     '''
#     A structured (additional) Description attribute, usable in multiple,
#     i.e. to simulate Dublin Core.  Usually from an external source.
#     '''
#     pass

#     TYPES = [
#         'abstract',
#         'subtitle',
#     ]

#
# Controlled Vocabulary
#

class Vocabulary(Base):
    '''A named, controlled vocabulary.'''
    
    name = models.CharField(max_length=255)


class Term(Base):
    '''
    A single Vocabulary term.

    This is an important class, used in other apps.  Be careful.
    '''
    
    name = models.CharField(max_length=255)
    vocabulary = models.ForeignKey('Vocabulary',
        on_delete=models.CASCADE,
        )


# class Language(Term):
#     '''The languages of the world.'''
#     pass


# class Unit(Term):
#     '''English and Metric units for space and time.'''
#     pass


# class Subject(Term):
#     '''Keywords, tags, and categories oh my.'''
#     pass


# class License(Term):
#     '''
#     Creative Commons, FOSS, and proprietary licenses,
#     defined against standard URLs.
#     '''
#     pass
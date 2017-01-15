from django.db import models
from base.models import Base


class Vocabulary(Base):
    '''A named, controlled vocabulary.'''
    
    name = models.CharField(max_length=255)


class Term(Base):
    '''
    A single Vocabulary term.
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
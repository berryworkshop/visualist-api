from django.db import models
from django.urls import reverse
from base.models import Record


class Page(Record):
    '''
    A general-purpose, arbitrary website page, e.g. About, Copyright, etc.
    '''
    
    name = models.CharField(max_length=100)
    synopsis = models.TextField(max_length=250, blank=True, null=True)
    body = models.TextField()


# class Article(Page):
#     '''A Page with a listed author, post date, and other blog-like features.'''
#     pass


# class Link(Record):
#     '''
#     A formal, named web link, usually to an external resource on the web.
#     '''
#     pass


# class RecordSet(Base):
#     '''A list of records for Users to share and save.'''
#     pass
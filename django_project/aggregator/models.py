from django.db import models
from cms.models import Record, Term, Base


class Source(Record):
    '''
    The object of a citation, e.g. an item of media, 
    a location on the internet, a book, a speech, or a conversation.
    '''
    pass


class RightSet(Base):
    '''A set of rules defining copyright for a Record.'''
    pass


class Service(Term):
    '''An online or social media service.'''
    pass
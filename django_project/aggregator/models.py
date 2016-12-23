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

# - - - - - - - - - - - - - - - - - - - - - - - - #

# round-trip
    # iCal

# import
    # iCal
# export
    #ical
# controlled vocabularies
    # Getty AAT
    # Getty TGN
    # LoC Subjects
    # Getty ULAN


def query_getty_aat(query):
    pass

def query_getty_tgn(query):
    pass

def query_getty_ulan(query):
    pass

def query_loc_subjects(query):
    pass
from django.db import models
from cms.models import Record, Term, Base


class Source(Record):
    '''Source'''
    pass


class Service(Term):
    '''Service'''
    pass


class Rights(Base):
    '''Rights'''
    pass


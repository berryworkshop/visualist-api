from django.db import models
from cms.models import Record, Term, Base


class Work(Record):
    '''Work'''
    pass


class Ephemeron(Work):
    '''Ephemeron'''
    pass


class Dimension(Base):
    '''Dimension'''
    pass


class Medium(Term):
    '''Medium'''
    pass


class Genre(Term):
    '''Genre'''
    pass


class Condition(Term):
    '''Condition'''
    pass


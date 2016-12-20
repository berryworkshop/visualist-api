from django.db import models
from cms.models import Record, Term, Base


class File(Record):
    '''File'''
    pass


class Image(File):
    '''Image'''
    pass


class Document(File):
    '''Document'''
    pass


class Video(File):
    '''Video'''
    pass


class ArchiveEvent(Base):
    '''ArchiveEvent'''
    pass


class Aspect(Term):
    '''Aspect'''
    pass


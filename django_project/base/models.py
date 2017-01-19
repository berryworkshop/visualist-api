from django.db import models
from django.utils.timezone import now

# This set of classes isn't really for direct use, but through subclasses.
# Should not have views, for example.


class Base(models.Model):
    '''
    Base class as a foundation for most others.
    '''
    
    class Meta:
        abstract = True
    
    created = models.DateTimeField(default=now)
    modified = models.DateTimeField(auto_now=True)
    # created_by = User.???


class Record(Base):
    '''
    The central class for the Visualist system; the basic unit manipulated
    by the User in the interface, often via "cards".
    '''
    
    class Meta:
        abstract = True

    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    # source may work implemented as a relation attribute
    # sources = models.ManyToManyField('base.Source', blank=True)

    # related_events = models.ManyToManyField('timeline.Event', blank=True)
    # related_venues = models.ManyToManyField('placefinder.Venue', blank=True)
    # related_works = models.ManyToManyField('catalog.Work', blank=True)
    # related_contacts = models.ManyToManyField('directory.Contact', blank=True)
    # related_pages = models.ManyToManyField('cms.Page', blank=True)

    def __str__(self):
        return self.name


class WorkContactJoin(models.Model):
    work = models.ForeignKey('catalog.Work', on_delete=models.CASCADE)
    contact = models.ForeignKey('directory.Contact', on_delete=models.CASCADE)
    RELATIONS = (
        ('CREATED','created by'),
        ('PUBLISHED','published by'),
        ('OWNED', 'owned by'),
        ('COLLECTION', 'in the collection of'),
    )
    relation_type = models.CharField(max_length=25, 
        choices=RELATIONS, default='CREATED')


class WorkEventJoin(models.Model):
    work = models.ForeignKey('catalog.Work', on_delete=models.CASCADE)
    event = models.ForeignKey('timeline.Event', on_delete=models.CASCADE)
    RELATIONS = (
        ('SHOWN','shown during'),
    )
    relation_type = models.CharField(max_length=25,
        choices=RELATIONS, default='SHOWN')


class WorkVenueJoin(models.Model):
    work = models.ForeignKey('catalog.Work', on_delete=models.CASCADE)
    venue = models.ForeignKey('placefinder.Venue', on_delete=models.CASCADE)
    RELATIONS = (
        ('SHOWN','shown at'),
    )
    relation_type = models.CharField(max_length=25,
        choices=RELATIONS, default='SHOWN')


class EventVenueJoin(models.Model):
    event = models.ForeignKey('timeline.Event', on_delete=models.CASCADE)
    venue = models.ForeignKey('placefinder.Venue', on_delete=models.CASCADE)
    RELATIONS = (
        ('HOSTED','hosted at'),
    )
    relation_type = models.CharField(max_length=25,
        choices=RELATIONS, default='SHOWN')


class EventContactJoin(models.Model):
    event = models.ForeignKey('timeline.Event', on_delete=models.CASCADE)
    contact = models.ForeignKey('directory.Contact', on_delete=models.CASCADE)
    RELATIONS = (
        ('PRODUCED','produced by'),
    )
    relation_type = models.CharField(max_length=25,
        choices=RELATIONS, default='PRODUCED')


class ContactVenueJoin(models.Model):
    contact = models.ForeignKey('directory.Contact', on_delete=models.CASCADE)
    venue = models.ForeignKey('placefinder.Venue', on_delete=models.CASCADE)
    RELATIONS = (
        ('OCCUPIED','occupant of'),
        ('OWNER','owner of'),
    )
    relation_type = models.CharField(max_length=25,
        choices=RELATIONS, default='OCCUPIED')


# class Source(Base):
#     '''
#     The object of a citation, e.g. an item of media, 
#     a location on the internet, a book, a speech, or a conversation.
#     '''

#     title = models.CharField(max_length=250)
#     author = models.CharField(max_length=250, blank=True)
#     publisher = models.CharField(max_length=250, blank=True)
#     date = models.CharField(max_length=250, blank=True)
#     place = models.CharField(max_length=250, blank=True)
#     URL = models.URLField(blank=True)
#     version = models.CharField(max_length=250, blank=True)
#     checked = models.DateField(blank=True, null=True)

#     TYPES = (
#         ('WEBSITE', 'website'),
#         ('BOOK', 'book'),
#         ('ARCHIVE', 'archive'),
#     )
#     source_type = models.CharField(max_length=250, choices=TYPES, blank=True)
#     notes = models.TextField(blank=True)

#     def populate_from_url(self):
#         # TODO
#         pass

#     def populate_from_previous(self):
#         # TODO
#         pass

#     def cite_mla(self):
#         # TODO
#         pass

#     def cite_chicago(self):
#         # TODO
#         pass


# class Log(Base):
#     '''Misc. website logs, for migrations, blame, among other things.'''
#     pass


# class Name(Base):
#     '''
#     A structured (additional) Name attribute, usable in multiple,
#     i.e. to simulate Dublin Core.  Usually from an external source.
#     '''

#     name = models.CharField(max_length=100)
#     records = models.ForeignKey('Record',
#         on_delete=models.CASCADE, related_name="names")


# class Identifier(Base):
#     '''
#     A structured (additional) Identifier attribute, usable in multiple,
#     i.e. to simulate Dublin Core.  Usually from an external source.
#     '''

#     identifier = models.CharField(max_length=255)
#     records = models.ForeignKey('Record', 
#         on_delete=models.CASCADE, related_name="identifiers")


# class Description(Base):
#     '''
#     A structured (additional) Description attribute, usable in multiple,
#     i.e. to simulate Dublin Core.  Usually from an external source.
#     '''

#     description = models.CharField(max_length=250)
#     records = models.ForeignKey('Record', 
#         on_delete=models.CASCADE, related_name="descriptions")


# class RecordRelation(Base):
#     '''
#     A connection to another local model, usually between Records
#     and their derivatives.
#     '''
#     pass
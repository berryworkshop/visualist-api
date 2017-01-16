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
    
    slug = models.CharField(max_length=100, unique=True)
    sources = models.ManyToManyField('Source', blank=True)

    def __str__(self):
        return self.slug


class Source(models.Model):
    '''
    The object of a citation, e.g. an item of media, 
    a location on the internet, a book, a speech, or a conversation.
    '''
    created = models.DateTimeField(default=now)
    modified = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, blank=True)
    publisher = models.CharField(max_length=250, blank=True)
    date = models.CharField(max_length=250, blank=True)
    place = models.CharField(max_length=250, blank=True)
    URL = models.URLField(blank=True)
    version = models.CharField(max_length=250, blank=True)
    checked = models.DateField(blank=True, null=True)

    TYPES = (
        ('WEBSITE', 'website'),
        ('BOOK', 'book'),
        ('ARCHIVE', 'archive'),
    )
    source_type = models.CharField(max_length=250, choices=TYPES, blank=True)
    notes = models.TextField(blank=True)

    def populate_from_url(self):
        # TODO
        pass

    def populate_from_previous(self):
        # TODO
        pass

    def cite_mla(self):
        # TODO
        pass

    def cite_chicago(self):
        # TODO
        pass


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

# Directory Contact
# Catalog Thing
# Calendar PointInTime
# Atlas PointInSpace


# class ContactThing(RecordRelation):
#     '''
#     Directory Contact <--> Catalog Thing
#     '''
#     pass


# class ContactThing(RecordRelation):
#     '''
#     Directory Contact <--> Catalog Thing
#     '''
#     pass
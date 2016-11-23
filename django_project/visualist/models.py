from django.db import models
from django.contrib.auth.models import User

# Auth
    # User
    # Group

# Visualist
    # Collection
        # Events
        # Media

# Dublin Core
    # Contributor
    # Coverage
    # Creator
    # Date
    # Description
    # Format
    # Identifier
    # Language
    # Publisher
    # Relation
    # Rights
    # Source
    # Subject
    # Title
    # Type

# Calendar
    # Event
    # Reminder

# Directory
    # Person
    # Organization

# Catalog
    # Work
    # Multimedia
        # Image
        # Video
        # Audio

# Category

# Map
    # Region
    # Place

class Base(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    #TODO: tags
    
    # def save(self):
    #     if not self.id:
    #         self.created = datetime.datetime.now()
    #     self.updated = datetime.datetime.now()
    #     super().save()


class Event(Base):
    when = models.DateTimeField()
    duration = models.IntegerField()
    venue = models.ForeignKey('Organization', models.SET_NULL)

    # not sure about these ones
    # on_site = models.BooleanField(default=True)
    # contact_name = ...
    # contact_email = ...

    # events can have sub-events, independent of main access hours. Optional.
    EVENT_TYPES = (
        ('EXHIBITION', 'exhibition'),
        ('READING', 'reading'),
        ('TALK', 'talk'),
        ('LECTURE', 'lecture'),
        ('PANEL', 'panel'),
        ('PERFORMANCE', 'performance'),
        ('OPENING', 'opening reception'),
        ('CLOSING', 'closing reception'),
        )
    event_type = models.CharField(max_length=15, choices=EVENT_TYPES)
    parent_event = models.ForeignKey('Event',
        models.CASCADE, related_name='child_events')

    # TODO: relationship to parent
    # TODO: integrate with iCal, gCal, etc.


class Entity(Base):
    class Meta:
        abstract = True

    born = models.DateField()
    lifespan = models.IntegerField(blank=True)

    # should Entities, Organizations, and Persons be in a separate app, a "directory"?
    # TODO: social media / websites
    # TODO: phones
    # TODO: emails


class OrganizationCategory(Base):
    '''
    A controlled vocabulary for Organization categories.
    '''
    CATEGORIES = (
        ('ARCHIVE', 'archive'),
        ('ASSOCIATION', 'center'),
        ('CONSORTIUM', 'consortium'),
        ('CORPORATION', 'corporation'),
        ('FOUNDATION', 'foundation'),
        ('GALLERY', 'gallery'),
        ('LIBRARY', 'library'),
        ('MUSEUM', 'museum'),
        ('SCHOOL', 'school'),
        )
    category = models.CharField(
        max_length=20,
        choices=CATEGORIES,
        default="GALLERY",
        unique=True
        )

    def __str__(self):
        return self.get_category_display()


class Organization(Entity):
    open_by_appointment = models.BooleanField()
    nonprofit = models.BooleanField()
    categories = models.ManyToManyField('OrganizationCategory', blank=True)
    loc_name_authority_id = models.IntegerField(blank=True)
    # TODO: hours


class Person(Entity):
    name = None
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    getty_ulan_id = models.IntegerField(blank=True)


class Location(Base):
    address = models.TextField()
    getty_tgn_id = models.IntegerField(blank=True)
    # TODO: GIS points


class Work(Base):
    pass

class Category(Base):
    pass


class Collection(Base):
    pass


class Multimedia(Base):
    pass
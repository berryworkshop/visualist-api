from django.db import models
from django.contrib.auth.models import User

# User
# Group

# Event
# Collection
    # Events
    # Media
# Work?
# Entity
    # Person
    # Organization
# Multimedia
    # Image
    # Video
    # Audio
# Category

# Map region
# Map place

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
    date = models.DateTimeField()
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

    lifespan = models.IntegerField(blank=True)

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
    address = models.TextField()
    open_by_appointment = models.BooleanField()
    nonprofit = models.BooleanField()
    incorporated = models.DateTimeField()
    categories = models.ManyToManyField('OrganizationCategory', blank=True)
    # TODO: hours

    loc_name_authority_id = models.IntegerField(blank=True)

    related_organizations = models.ManyToManyField('Organization',
        through='OrgOrgRelationship',
        through_fields=('parent', 'child'),
        symmetrical=False,
        blank=True,
        )


class OrgOrgRelationship(models.Model):
    class Meta:
        verbose_name='organization relationship'
    born = models.DateTimeField()
    parent = models.ForeignKey('Organization',
        on_delete=models.CASCADE,
        related_name='child_relation_set', # from related parent
        )
    child = models.ForeignKey('Organization',
        on_delete=models.CASCADE,
        related_name='parent_relation_set', # from related child
        )
    CATEGORIES = (
        ('DEPARTMENT', 'is department of'), 
        ('LOCATED', 'is located in'), 
        ('MEMBER', 'is member of'), 
        ('OWNED', 'is owned by'), 
        ('PART', 'is part of'), 
        )
    category = models.CharField(
        max_length=50,
        choices=CATEGORIES,
        default='DEPARTMENT',   
        )

    # TODO: validate combination of parent and child?


class Person(Entity):
    name = None
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    getty_ulan_id = models.IntegerField(blank=True)


class Location(Base):    
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
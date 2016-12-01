from django.db import models
from django.contrib.auth.models import User


# Notes
    # All fields which pull from external sources should be sourced: Citation


# Events
    # date start
    # date end
    # Receptions
    # names
    # Venue -> org
    # Facebook links
    # weblinks
# Artists
    # Names
# Pictures
    # largely limited to a single postcard-esque image per show
# Venues
    # Name
    # Address
    # Hours (comma separated)
    # By appointment (y/n)
    # Website
    # Facebook page

# Services/ APIs
    # Art Institute of Chicago
    # Art Fact City
    # Art Forum
    # Art In America
    # Art Journal
    # Art News
    # College Art Association
    # Chicago Artist Writers
    # Chicago Artists Resource
    # Chicago gallery news
    # Chicago Reader
    # Chicago Tribune
    # Code4Lib
    # Crains
    # Dialogue
    # DNAInfo
    # Facebook
    # Getty Art and Architecture Thesaurus
    # Getty Union List of Artist Names
    # Getty Thesaurus of Geographic Names
    # Chicago Public Library
    # Hyde Park Herald
    # Hyperallergic
    # Library of Congress Subject Headings
    # New Art Examiner
    # New City
    # October
    # PForm
    # RedEye
    # South Side Weekly
    # TimeOut

# Citation
    # Author
    # Date
    # Publisher
    # Title
    # Place
    # URL
    # Version
    # Type
    # etc.?
        # Consult APA, Chicago, MLA guidelines to ensure we have sufficient data

# Potential Data
#---
# Dates
# Neighborhoods
# From Allan
    # More info for artists?
        # Dates?
        # Hometown?
        # Specialties?
    # Individual artworks?
        # Values?
        # Media?
    # Hashtags/Keywords?  (non-hierarchical structure, for sorting/finding)
    # Categories? (hierarchical structure, for browsing).  Existing (overlapping) rhizomatic hierarchies:
        # Neighborhoods
        # Event types
        # etc.
    # Event Collections?
# Events
    # Title
    # Venue
    # Address
    # City, State, Zip
    # Phone
    # Email
    # Web
    # Admission Fee
    # Group-friendly
        # Tiered?
    # Kind of Event
        # Exhibition
            # Opening Date
            # Closing Date
            # Reception Date
            # Reception Time
            # description
            # Image
            # Facebook link
        # Reading
            # Date(s)
            # Time
            # Description
            # Image
            # Facebook link
        # Lecture/Panel/Artist Talk
            # Date(s)
            # Time
            # Description
            # Image
            # Facebook link
        # Performance
            # Date(s)
            # Time
            # Description
            # Image
            # Facebook link
    # Are there other programs associated with this event (y/n)
        # If yes
        # How many? (Adds the amount of drop downs needed)
        # Title
        # Date
        # Time
        # Kind of Event
            # Exhibition
            # Reading
            # Lecture
            # Performance
        # Facebook link
        # Description
        # Is this event on-site (y/n)
    # If not
        # Venue
        # Address
        # City, State, Zip
        # Phone 
        # Email
        # Web
        # For internal use only
            # Contact name
            # Contact email
# Other media
    # video fills
    # alternate image file types
        # (currently we can only upload .jpg)
        # gif files
    # Audio
    # photo albums
# web links
    # Calendar We’d like to be able to incorporate some calendar data into maps.
    # Google
    # Ical
    # Yahoo
    # Facebook
    # Outlook

# Auth
    # User
    # Group

# Visualist
    # Collection
        # Events
        # Media

# Person
    # Think “Artist” or “Gallerist”.  A Person can be anyone involved in a Venue or Event
    # Has many Events
    # Has many Venues
    # dates
    # alias (Madonna)
# Event
    # Has one Venue
    # Has many People
    # dates
    # sub-events: parties, openings, closings
        # defaults: parent Event
    # pricing
# Venue
    # Has many Events
    # Has many People
    # dates
    # pricing
    # independence: gradient between 0: institutional and 1: independent
# User
    # Has many Tours
    # Has many Venues
# Tour
    # An ordered collection of Events and/or Venues
    # Has one User
    # Has many Events
    # Has many Venues

# Ephemera


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
        # Website/Software
        # Object/Hardware
        # Performance
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
    # duration = models.IntegerField()
    venue = models.ForeignKey('Organization', models.SET_NULL)

    # not sure about these ones
    # on_site = models.BooleanField(default=True)
    # contact_name = ...
    # contact_email = ...

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

    # TODO: relationship to parent
    # TODO: integrate with iCal, gCal, etc.


class Entity(Base):
    class Meta:
        abstract = True

    born = models.DateField()
    # lifespan = models.IntegerField(blank=True)

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
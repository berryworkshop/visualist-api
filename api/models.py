from django.db import models


class Resource(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )
    name = models.TextField()
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.name


class License(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )
    name = models.TextField()
    url = models.URLField(
        blank=True,
    )

    def __str__(self):
        return self.name


class Base(models.Model):
    class Meta:
        abstract = True
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )
    source = models.ForeignKey('Resource')
    license = models.ForeignKey('License')


class Image(Base):
    schema = 'http://schema.org/ImageObject'
    ASPECTS = (
        ('main', 'Main'),
        ('recto', 'Recto'),
        ('verso', 'Verso'),
        ('detail', 'detail'),
        ('signature', 'signature'),
    )
    title = models.TextField()
    aspect = models.TextField(
        choices=ASPECTS,
        default='main',
    )
    checksum = models.TextField()

    def __str__(self):
        return self.title


class ContactItem(Base):
    class Meta:
        abstract = True


class Address(ContactItem):
    ISO_3166_2 = (
      ('IL', 'Illinois'),
      ('IN', 'Indiana'),
      ('MI', 'Michigan'),
      ('WI', 'Wisconsin'),
    )
    address_for = models.ForeignKey('Record',
        related_name='addresses',
    )
    address_street = models.TextField()
    address_locality = models.TextField()
    address_region = models.TextField(
        choices=ISO_3166_2,
    )
    address_postal_code = models.TextField()
    address_country = models.ForeignKey('Nationality')
    # latitude = models.DecimalField()
    # longitude = models.DecimalField()

    def __str__(self):
        return '{}, {} {}, {}'.format(
            self.address_street, self.address_locality, self.address_region,
            self.address_postal_code)


class Phone(ContactItem):
    phone_for = models.ForeignKey('Record')
    country = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    exchange = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    extension = models.PositiveIntegerField()

    def __str__(self):
        return '{} ({}) {}-{} x{}'.format(
            self.country, self.area, self.exchange,
            self.number, self.extension)


class Email(ContactItem):
    email_for = models.ForeignKey('Record')
    value = models.TextField()

    def __str__(self):
        return self.value


class SocialAccount(Base):
    account_for = models.ForeignKey(
        'Record',
        related_name='accounts',
    )
    SERVICES = (
      ('ask', 'Ask.fm'),
      ('facebook', 'Facebook'),
      ('flickr', 'Flickr'),
      ('foursquare', 'Foursquare'),
      ('github', 'GitHub'),
      ('googleplus', 'Google+'),
      ('instagram', 'Instagram'),
      ('linkedin', 'LinkedIn'),
      ('meetup', 'Meetup'),
      ('pinterest', 'Pinterest'),
      ('reddit', 'Reddit'),
      ('snapchat', 'SnapChat'),
      ('tumblr', 'Tumblr'),
      ('twitter', 'Twitter'),
      ('vine', 'Vine'),
      ('whatsapp', 'WhatsApp'),
      ('yelp', 'Yelp'),
      ('youtube', 'YouTube'),
    )
    service = models.TextField(
        choices=SERVICES,
    )
    value = models.TextField()

    def __str__(self):
        return '{}: {}'.format(self.service, self.value)


class Snippet(Base):
    value = models.TextField()

    def __str__(self):
        return self.value


class Category(Base):
    value = models.TextField()
    parent = models.ForeignKey('self',
        related_name='children',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.value


class Tag(Base):
    value = models.SlugField()

    def __str__(self):
        return self.value


class Identifier(Base):
    value = models.TextField()

    def __str__(self):
        return self.value


class Nationality(Base):
    ISO_3166_1 = (
      ('US', 'United States of America'),
      ('CA', 'Canada'),
      ('MX', 'Mexico'),
    )
    value = models.TextField(
        choices=ISO_3166_1,
    )

    def __str__(self):
        return self.value


CATEGORIES = {
    'event': [
        'course',
        'exhibition',
        'performance',
        'reception',
        'residency',
        'workshop',
    ],
    'work': [
        'article',
        'book',
        'installation',
        'photograph',
        'sculpture',
        'visual artwork',
        'website',
    ],
    'person': [
        'artist',
        'writer',
        'architect',
        'filmmaker',
        'curator',
        'gallerist',
        'professor',
    ],
    'organization': [
        'archive',
        'association',
        'company',
        'consortium',
        'foundation',
        'library',
        'museum',
        'school',
    ],
    'page': [
        'article',
        'review',
    ],
    'collection': [
        'tour'
    ],
}


class Record(Base):
    schema = 'http://schema.org/Thing'

    slug = models.SlugField()
    categories = models.ManyToManyField('Category')
    description = models.ForeignKey('Snippet')
    featured = models.BooleanField(
        default=False,
    )
    approved = models.BooleanField(
        default=False,
    )
    web_public = models.BooleanField(
        default=True,
    )
    same_as = models.URLField(
        blank=True,
    )
    tags = models.ManyToManyField('Tag',
        blank=True,
    )
    identifiers = models.ManyToManyField('Identifier',
        blank=True,
    )
    images = models.ManyToManyField('Image',
        blank=True,
    )

    def __str__(self):
        return self.slug

    def name():
        pass

    def age():
        pass

    def citation():
        pass

    def date():
        pass

    def get_absolute_url():
        pass

    def location():
        pass

    def distance():
        pass


class Event(Record):
    schema = 'http://schema.org/Event'

    STATUSES = (
        ('active', 'active'),
        ('cancelled', 'cancelled'),
    )
    name = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(
        blank=True,
    )
    status = models.TextField(
        choices=STATUSES,
        default='active',
    )
    group_friendly = models.NullBooleanField(
        blank=True,
    )
    parent = models.ForeignKey('self',
        related_name='children',
        blank=True,
        null=True,
    )
    organizers = models.ManyToManyField('Entity',
        related_name='organizer_of',
        blank=True,
    )
    curators = models.ManyToManyField('Entity',
        related_name='curator_of',
        blank=True,
    )
    producers = models.ManyToManyField('Entity',
        related_name='producer_of',
        blank=True,
    )
    exhibitors = models.ManyToManyField('Entity',
        related_name='exhibitor_at',
        blank=True,
    )
    contributors = models.ManyToManyField('Entity',
        related_name='contributor_to',
        blank=True,
    )

    def __str__(self):
        return self.name

    def duration():
        pass


class Work(Record):
    schema = 'http://schema.org/CreativeWork'

    name = models.TextField()
    completed = models.DateTimeField(
        blank=True,
    )
    published = models.DateTimeField(
        blank=True,
    )
    version = models.TextField(
        blank=True,
    )
    url = models.URLField(
        blank=True,
    )
    created_at = models.ManyToManyField('Place',
        related_name='works_created_here',
        blank=True,
    )
    location = models.ManyToManyField('Place',
        related_name='works_here',
        blank=True,
    )

    def __str__(self):
        return self.name


class Entity(Record):
    works = models.ManyToManyField('Work',
        related_name='creator',
        blank=True,
    )


class Person(Entity):
    schema = 'http://schema.org/Person'

    GENDERS = (
        ('m', 'male'),
        ('f', 'female'),
        ('x', 'x'),
    )
    name_first = models.TextField(
        blank=True,
    )
    name_last = models.TextField()
    born = models.DateTimeField(
        blank=True,
        null=True,
    )
    died = models.DateTimeField(
        blank=True,
        null=True,
    )
    gender = models.TextField(
        choices=GENDERS,
        blank=True,
    )
    born_at = models.ForeignKey('Place',
        related_name='birthplace_of',
        blank=True,
        null=True,
    )
    died_at = models.ForeignKey('Place',
        related_name='deathplace_of',
        blank=True,
        null=True,
    )
    nationalities = models.ManyToManyField('Nationality',
        blank=True,
    )
    parents = models.ManyToManyField('self',
        related_name='children',
        blank=True,
    )
    friends = models.ManyToManyField('self',
        blank=True,
    )

    def __str__(self):
        return '{}, {}'.format(self.name_last, self.name_first)


class Organization(Entity):
    schema = 'http://schema.org/Organization'

    name = models.TextField()
    founded = models.DateTimeField(
        blank=True,
    )
    founded_at = models.ForeignKey('Place',
        blank=True,
        null=True,
    )
    dissolved = models.DateTimeField(
        blank=True,
    )
    nonprofit = models.NullBooleanField()
    appointment_only = models.BooleanField(
        default=False,
    )
    hours = models.TextField(
        blank=True,
    )
    logo = models.ForeignKey('Image',
        blank=True,
        null=True,
    )
    members = models.ManyToManyField('Entity',
        related_name='member_of',
        blank=True,
    )
    parent = models.ForeignKey('self',
        related_name='children',
        blank=True,
        null=True,
    )
    members = models.ManyToManyField('Entity',
        related_name='member_of',
        blank=True,
    )
    artists = models.ManyToManyField('Entity',
        related_name='represented_by',
        blank=True,
    )
    employees = models.ManyToManyField('Person',
        related_name='employed_by',
        blank=True,
    )

    def __str__(self):
        return self.name


class Place(Record):
    schema = 'http://schema.org/Place'

    name = models.TextField()
    body = models.ForeignKey('Snippet',
        blank=True,
        null=True,
    )
    events = models.ManyToManyField('Event',
        related_name='has_venue',
        blank=True,
    )

    def __str__(self):
        return self.name


class Post(Record):
    name = models.TextField()
    parent = models.ForeignKey('self',
        related_name='children',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Page(Post):
    schema = 'http://schema.org/WebPage'

    body = models.ForeignKey('Snippet')


class Collection(Post):
    schema = 'http://schema.org/CollectionPage'
    records = models.ManyToManyField('Record')


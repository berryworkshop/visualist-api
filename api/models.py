from django.db import models

# todo:
    # PyDoc for classes
    # help_text for fields


class Base(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )


class Resource(Base):

    name = models.CharField(
        max_length=250
    )
    description = models.TextField()
    url = models.URLField(
        blank=True,
        unique=True
    )

    def __str__(self):
        return self.name


class License(Base):

    name = models.CharField(
        unique=True,
        max_length=250,
    )
    url = models.URLField(
        blank=True,
        unique=True
    )

    def __str__(self):
        return self.name


class Nationality(Base):
    class Meta:
        verbose_name_plural = 'nationalities'
        ordering = ['value']

    ISO_3166_1 = (
      ('US', 'United States of America'),
      ('CA', 'Canada'),
      ('MX', 'Mexico'),
    )
    value = models.CharField(
        max_length=2,
        choices=ISO_3166_1,
        unique=True,
    )

    def __str__(self):
        return self.value

class Sourced(Base):
    class Meta:
        abstract = True

    source = models.ForeignKey('Resource')


class Image(Sourced):

    schema = 'http://schema.org/ImageObject'
    license = models.ForeignKey('License')
    ASPECTS = (
        ('main', 'Main'),
        ('recto', 'Recto'),
        ('verso', 'Verso'),
        ('detail', 'detail'),
        ('signature', 'signature'),
    )
    title = models.CharField(
        max_length=250,
    )
    aspect = models.CharField(
        max_length=25,
        choices=ASPECTS,
        default='main',
    )
    checksum = models.CharField(
        max_length=250,
        unique=True
    )

    def __str__(self):
        return self.title


class ContactItem(Sourced):
    class Meta:
        abstract = True
        ordering = ['-created',]


class Address(ContactItem):
    class Meta:
        verbose_name_plural = 'addresses'
        unique_together = (
            ("address_street", "address_locality", "address_region"),
        )

    ISO_3166_2 = (
      ('IL', 'Illinois'),
      ('IN', 'Indiana'),
      ('MI', 'Michigan'),
      ('WI', 'Wisconsin'),
    )
    address_street = models.TextField()
    address_locality = models.CharField(
        max_length=250,
    )
    address_region = models.CharField(
        max_length=2,
        choices=ISO_3166_2,
    )
    address_postal_code = models.CharField(
        max_length=250,
    )
    address_country = models.ForeignKey('Nationality')
    # latitude = models.DecimalField()
    # longitude = models.DecimalField()

    def __str__(self):
        return '{}, {} {}, {}'.format(
            self.address_street, self.address_locality, self.address_region,
            self.address_postal_code)


class Phone(ContactItem):
    class Meta:
        unique_together = (
            ("phone_for", "country", "area", "exchange", "number"),)

    phone_for = models.ForeignKey('Record')
    country = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    exchange = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    extension = models.PositiveIntegerField()

    def __str__(self):
        return '{} ({}) {}-{} x{}'.format(
            self.country,
            self.area,
            self.exchange,
            self.number,
            self.extension
        )


class Email(ContactItem):

    email_for = models.ForeignKey('Record')
    value = models.EmailField(
        unique=True
    )

    def __str__(self):
        return self.value


class SocialAccount(Base):
    class Meta:
        unique_together = (
            ("service", "value"),
        )

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
    service = models.CharField(
        max_length=25,
        choices=SERVICES,
    )
    value = models.CharField(
        max_length=250,
    )

    def __str__(self):
        return '{}: {}'.format(self.service, self.value)


class Snippet(Sourced):

    value = models.TextField()
    license = models.ForeignKey('License')

    def __str__(self):
        return self.value


class Category(Base):
    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['value']
        unique_together = (
            ("value", "parent"),
        )

    value = models.CharField(
        max_length=250,
    )
    parent = models.ForeignKey('self',
        related_name='children',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.value


class Tag(Base):
    class Meta:
        ordering = ['value']

    value = models.SlugField(
        unique=True
    )

    def __str__(self):
        return self.value


class Identifier(Base):
    class Meta:
        ordering = ['-created']

    value = models.CharField(
        max_length=250,
    )
    record = models.ForeignKey('Record')

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


class Record(Sourced):

    schema = 'http://schema.org/Thing'
    license = models.ForeignKey('License')

    slug = models.SlugField(
        unique=True
    )
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
    images = models.ManyToManyField('Image',
        blank=True,
    )
    addresses = models.ManyToManyField('Address',
        blank=True,
    )

    def __str__(self):
        return '{}'.format(self.slug)

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
    class Meta:
        ordering = ['-date_start', '-date_end', 'name']

    schema = 'http://schema.org/Event'

    STATUSES = (
        ('active', 'active'),
        ('cancelled', 'cancelled'),
    )
    name = models.CharField(
        max_length=250,
    )
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(
        blank=True,
    )
    status = models.CharField(
        max_length=25,
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
        return 'event: {}'.format(self.name)

    def duration():
        pass


class Work(Record):
    class Meta:
        ordering = ['name', '-created']

    schema = 'http://schema.org/CreativeWork'

    name = models.CharField(
        max_length=250,
    )
    completed = models.DateTimeField(
        blank=True,
    )
    published = models.DateTimeField(
        blank=True,
    )
    version = models.CharField(
        max_length=250,
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
        return 'work: {}'.format(self.name)


class Entity(Record):

    works = models.ManyToManyField('Work',
        related_name='creator',
        blank=True,
    )


class Person(Entity):
    class Meta:
        verbose_name_plural = 'people'
        ordering = ['name_last', 'name_first', '-created']

    schema = 'http://schema.org/Person'

    GENDERS = (
        ('m', 'male'),
        ('f', 'female'),
        ('x', 'x'),
    )
    name_first = models.CharField(
        max_length=250,
        blank=True,
    )
    name_last = models.CharField(
        max_length=250,
    )
    born = models.DateTimeField(
        blank=True,
        null=True,
    )
    died = models.DateTimeField(
        blank=True,
        null=True,
    )
    gender = models.CharField(
        max_length=1,
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
        return 'person: {}, {}'.format(self.name_last, self.name_first)


class Organization(Entity):
    class Meta:
        ordering = ['name', '-created']

    schema = 'http://schema.org/Organization'

    name = models.CharField(
        max_length=250,
    )
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
        return 'org: {}'.format(self.name)


class Place(Record):
    class Meta:
        ordering = ['name', '-created']

    schema = 'http://schema.org/Place'

    name = models.CharField(
        max_length=250,
    )
    body = models.ForeignKey('Snippet',
        blank=True,
        null=True,
    )
    events = models.ManyToManyField('Event',
        related_name='has_venue',
        blank=True,
    )

    def __str__(self):
        return 'place: {}'.format(self.name)


class Post(Record):
    class Meta:
        ordering = ['name', '-created']

    name = models.CharField(
        max_length=250,
    )
    parent = models.ForeignKey('self',
        related_name='children',
        blank=True,
        null=True,
    )

    def __str__(self):
        return 'post: {}'.format(self.name)


class Page(Post):
    class Meta:
        ordering = ['-created']

    schema = 'http://schema.org/WebPage'
    body = models.ForeignKey('Snippet')

    def __str__(self):
        return 'page: {}'.format(self.name)


class Collection(Post):
    class Meta:
        ordering = ['-created']

    schema = 'http://schema.org/CollectionPage'
    records = models.ManyToManyField('Record')

    def __str__(self):
        return 'coll: {}'.format(self.name)


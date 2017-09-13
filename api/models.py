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


class Sourced(models.Model):
    class Meta:
        abstract = True

    source = models.ForeignKey('Work',
        blank=True,
    )


class Hierarchical(models.Model):
    class Meta:
        abstract = True

    parent = models.ForeignKey('self',
        related_name='children',
        blank=True,
        null=True,
    )


class Image(Base, Sourced):

    schema = 'http://schema.org/ImageObject'
    name = models.CharField(
        max_length=250,
    )
    ASPECTS = (
        ('main', 'Main'),
        ('recto', 'Recto'),
        ('verso', 'Verso'),
        ('detail', 'detail'),
        ('signature', 'signature'),
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
        return self.name


class Address(Base, Sourced):
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
    address_country = models.ForeignKey('Term')
    # latitude = models.DecimalField()
    # longitude = models.DecimalField()

    def __str__(self):
        return '{}, {} {}, {}'.format(
            self.address_street, self.address_locality, self.address_region,
            self.address_postal_code)


class Phone(Base, Sourced):
    class Meta:
        unique_together = (
            ("area", "exchange", "number"),
        )

    country = models.PositiveIntegerField(
        default=1,
    )
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


class Email(Base, Sourced):

    value = models.EmailField(
        unique=True
    )

    def __str__(self):
        return self.value


class SocialAccount(Base, Sourced):
    class Meta:
        unique_together = (
            ("service", "value"),
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


class Snippet(Base, Sourced):

    value = models.TextField()
    license = models.ForeignKey('Work',
        related_name='licensed_snippets'
    )

    def __str__(self):
        return self.value


class Term(Base, Hierarchical):
    class Meta:
        ordering = ['value']
        unique_together = (
            ("value", "vocabulary"),
            ("value", "parent"),
        )

    vocabulary = models.ForeignKey('Work')
    value = models.CharField(
        max_length=250,
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
        'vocabulary',
        'license',
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



class Label(models.Model):
    pass



class Relation(models.Model):
    PREDICATES = (
        (('parent'), ('parent of')),
        (('category'), ('category for')),
        (('member'), ('member of')),

        # general
        (('creator'), ('creator of')),
        (('contributor'), ('contributor to')),

        # event
        (('organizer'), ('organizer of')),
        (('curator'), ('curator of')),
        (('exhibitor'), ('exhibitor of')),
        (('producer'), ('producer of')),

        # work
        (('publisher'), ('publisher of')),
    )
    subject = models.ForeignKey(Record, on_delete=models.PROTECT)
    predicate = models.CharField(
        options=PREDICATES,
    )
    dobject = models.ForeignKey(Record, on_delete=models.PROTECT)



class Record(Base, Sourced):

    # schema = 'http://schema.org/Thing'

    # basic
    name = models.CharField(
        max_length=250,
    )
    slug = models.SlugField(
        unique=True
    )
    description = models.ForeignKey('Snippet')
    same_as = models.URLField(
        blank=True,
    )
    start = models.DateTimeField()
    end = models.DateTimeField(
        blank=True,
    )

    # properties
    # categories = models.ManyToManyField('self',
    #     through='Relation', through_fields=('subject', 'dobject'),
    # )
    labels = models.ManyToManyField('Label')
    tags = models.ManyToManyField('Tag',
        blank=True,
    )
    images = models.ManyToManyField('Image',
        blank=True,
    )

    # meta
    license = models.ForeignKey('self',
        related_name='licensed_records'
    )
    status = models.NullBooleanField(
        blank=True,
    )
    featured = models.BooleanField(
        default=False,
    )
    approved = models.BooleanField(
        default=False,
    )
    web_public = models.BooleanField(
        default=True,
    )

    # contact info
    addresses = models.ManyToManyField('Address',
        blank=True,
    )
    phones = models.ManyToManyField('Phone',
        blank=True,
    )
    emails = models.ManyToManyField('Email',
        blank=True,
    )
    social_accounts = models.ManyToManyField('SocialAccount',
        blank=True,
    )

    # event fields
    organizers = models.ManyToManyField('self',
        through='Relation', through_fields=('subject', 'dobject'),
        blank=True
    )
    curators = models.ManyToManyField('self',
        through='Relation', through_fields=('subject', 'dobject'),
        blank=True
    )
    producers = models.ManyToManyField('self',
        through='Relation', through_fields=('subject', 'dobject'),
        blank=True
    )
    exhibitors = models.ManyToManyField('self',
        through='Relation', through_fields=('subject', 'dobject'),
        blank=True
    )
    contributors = models.ManyToManyField('self',
        through='Relation', through_fields=('subject', 'dobject'),
        blank=True
    )

    # methods
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



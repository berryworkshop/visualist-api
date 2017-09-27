from django.db import models
from django.contrib.postgres import fields as pg

# todo:
    # PyDoc for classes
    # help_text for fields


class Base(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    modified_on = models.DateTimeField(
        auto_now=True,
    )


class Resource(Base):
    title = models.CharField(
        max_length=250,
    )
    description = models.TextField(
        blank=True,
    )
    url = models.URLField(
        blank=True,
    )

    def __str__(self):
        return self.title


class License(Base):
    title = models.CharField(
        max_length=250,
    )
    description = models.TextField(
        blank=True,
    )
    url = models.URLField(
        blank=True,
    )

    def __str__(self):
        return self.title



class Sourced(models.Model):
    class Meta:
        abstract = True

    source = models.ForeignKey('Resource',
        blank=True,
        null=True,
    )


class Hierarchical(models.Model):
    class Meta:
        abstract = True

    parent = models.ForeignKey('self',
        related_name='children',
        blank=True,
        null=True,
    )


# class Name(Base, Sourced):

#     record = models.ForeignKey('Record')
#     primary = models.CharField(
#         max_length = 250,
#     )
#     secondary = models.CharField(
#         max_length = 250,
#         blank=False,
#     )

#     def __str__(self):
#         return self.value


class Image(Base, Sourced):
    schema = 'http://schema.org/ImageObject'
    title = models.CharField(
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


class Term(Base, Hierarchical):
    class Meta:
        unique_together = (
            ("value", "vocabulary"),
            ("value", "parent"),
        )

    vocabulary = models.ForeignKey('Resource')
    value = models.CharField(
        max_length=250,
    )

    def __str__(self):
        return self.value


class Tag(Base):
    value = models.SlugField(
        unique=True
    )

    def __str__(self):
        return self.value


class Identifier(Base):
    value = models.CharField(
        max_length=250,
    )
    record = models.ForeignKey('Record')

    def __str__(self):
        return self.value


class Relation(models.Model):

    PREDICATES = (
        # item-level
            # relations flow in this direction, when possible
                # Event
                # Work
                # Organization
                # Person
                # Place
                # Page

            # event
            # (('has_event'), ('has event')), # reverse

            # work
            # (('has_work'), ('has work')), # reverse

            # person/organization
            (('has_contributor'), ('has contributor')),
            (('has_creator'), ('has creator')),
            (('has_curator'), ('has curator')),
            (('has_employee'), ('has employee')),
            (('has_exhibitor'), ('has exhibitor')),
            (('has_friend'), ('has friend')),
            (('has_member'), ('has member')),
            (('has_organizer'), ('has organizer')),
            (('has_owner'), ('has owner')),
            (('has_parent'), ('has parent')),
            (('has_producer'), ('has producer')),
            (('has_publisher'), ('has publisher')),
            (('has_affiliation'), ('has affiliation')),
            (('has_spouse'), ('has spouse')),
            (('has_venue'), ('has_venue')),

            # place
            (('located_at'), ('located at')),
            (('started_at'), ('started at')),
            (('ended_at'), ('ended at')),
            (('born_at'), ('born at')),
            (('died_at'), ('died at')),

            # generic
            (('part_of'), ('part of')),
            (('same_as'), ('same as')),

        # meta-level
        (('has_record_source'), ('has record source')),
        (('has_record_parent'), ('has record parent')),
        (('has_record_owner'), ('has record owner')),
        (('has_record_category'), ('has record category')),
        (('has_record_submitter'), ('has record submitter')),
    )
    subject = models.ForeignKey('Record',
        related_name='relation_subject',
        on_delete=models.PROTECT,
    )
    predicate = models.CharField(
        choices=PREDICATES,
        max_length=25,
    )
    dobject = models.ForeignKey('Record',
        related_name='relation_direct_object',
        on_delete=models.PROTECT,
    )
    properties = pg.JSONField(
        default=dict(),
    )
    dates = pg.DateTimeRangeField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return '( {} )-[ {} ]->( {} )'.format(self.subject, self.predicate, self.dobject)


class Record(Base, Sourced):
    class Meta:
        ordering = [
            '-created_on',
        ]

    schema = 'http://schema.org/Thing'

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

    LABELS = (
        (('event'), ('event')),
        (('work'), ('work')),
        (('person'), ('person')),
        (('organization'), ('organization')),
        (('page'), ('page')),
        (('collection'), ('collection')),
    )

    related = models.ManyToManyField('self',
        through='Relation',
        through_fields=('subject', 'dobject'),
        symmetrical=False,
        blank=True
    )

    # classification
    # title = models.CharField(
    #     max_length=250,
    # )
    slug = models.SlugField(
        unique=True,
    )
    # body = models.TextField(
    #     blank=True,
    # )
    # url = models.URLField(
    #     blank=True,
    # )
    # categories = models.ManyToManyField('self',
    #     through='Relation', through_fields=('subject', 'dobject'),
    # )
    label = models.CharField(
        max_length=25,
        choices=LABELS,
    )
    tags = models.ManyToManyField('Tag',
        blank=True,
    )
    images = models.ManyToManyField('Image',
        blank=True,
    )
    license = models.ForeignKey('License',
        related_name='records_licensed',
    )

    properties = pg.JSONField(
        default=dict(),
    )

    # common
    # lifespan = pg.DateRangeField()
    # duration = pg.DateTimeRangeField()

    # meta
    # version = models.CharField(
    #     max_length=250,
    #     blank=True,
    #     default="1.0"
    # )
    is_active = models.BooleanField(
        default=True,
    )
    is_featured = models.BooleanField(
        default=False,
    )
    is_approved = models.BooleanField(
        default=False,
    )
    is_web_public = models.BooleanField(
        default=True,
    )

    # contact info
    # addresses = models.ManyToManyField('Address',
    #     blank=True,
    # )
    # phones = models.ManyToManyField('Phone',
    #     blank=True,
    # )
    # emails = models.ManyToManyField('Email',
    #     blank=True,
    # )
    # social_accounts = models.ManyToManyField('SocialAccount',
    #     blank=True,
    # )

    # event fields
    # is_group_friendly = models.NullBooleanField(
    #     blank=True,
    # )

    # work fields
    # published_on = models.DateField(
    #     blank=True,
    # )

    # person fields
    # GENDERS = (
    #     ('m', 'male'),
    #     ('f', 'female'),
    #     ('x', 'x'),
    # )
    # gender = models.CharField(
    #     max_length=1,
    #     choices=GENDERS,
    #     blank=True,
    # )

    # organization fields
    # is_nonprofit = models.NullBooleanField(
    #     blank=True,
    #     default=None,
    # )
    # by_appointment_only = models.NullBooleanField(
    #     blank=True,
    #     default=None,
    # )

    # methods
    def __str__(self):
        return '{}: {}'.format(self.label, self.slug)

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

    def duration():
        pass



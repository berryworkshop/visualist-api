from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres import fields as pg
from cerberus import Validator
from .schemas.record import (
    work_schema,
    event_schema,
    person_schema,
    organization_schema,
)
from .schemas.relation import (
    relation_schema,
    reference_schema,
)
from .schemas.etc import (
    source_schema,
)


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


class Image(Base):
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
    source = models.ForeignKey('Record',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Term(Base):
    value = models.CharField(
        max_length=250
    )
    slug = models.SlugField(
        unique=True
    )
    # LABELS = (
    #     ('tag', 'tag'),
    #     ('category', 'category'),
    #     ('identifier', 'identifier'),
    # )
    # label = models.CharField(
    #     max_length=25,
    #     choices=LABELS,
    #     blank=False,
    #     null=False
    # )
    VOCABULARIES = (
        ('visualist', 'The Visualist'),
        ('aat', 'Getty Art and Architecture Thesaurus'),
        ('ulan', 'Getty Union List of Artist Names'),
        ('lccn', 'Library of Congress Control Number'),
        ('viaf', 'Virtual International Authority File'),
    )
    vocabulary = models.CharField(
        max_length=25,
        choices=VOCABULARIES,
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    canonical_url = models.URLField(
        blank=True,
        null=True,
    )
    parent = models.ForeignKey('self',
        related_name='children',
        blank=True,
        null=True,
    )
    same_as = models.ManyToManyField('self',
        blank=True,
    )

    def __str__(self):
        if self.vocabulary:
            vocab = self.vocabulary.upper() + ': '
        else:
            vocab = ''
        return '{}{}'.format(vocab, self.value)


class Date(Base):
    class Meta:
        unique_together = (
            ("date", "precision_days"),
        )

    date = models.DateField()
    precision_days = models.PositiveIntegerField(
        # https://goo.gl/vA8HD8
        default=0
    )

    def __str__(self):
        return str(self.date)


class Location(Base):
    class Meta:
        unique_together = (
            ("latitude", "longitude", "altitude"),
        )

    latitude = models.DecimalField(
        decimal_places=7,
        max_digits=10,
    )
    longitude = models.DecimalField(
        decimal_places=7,
        max_digits=10,
    )
    altitude = models.DecimalField(
        decimal_places=7,
        max_digits=10,
        blank=True,
        null=True,
    )
    street = models.TextField(
        blank=True,
        null=True,
    )
    locality = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        default='Chicago',
    )
    REGIONS = (
        ('IL','Illinois'),
        ('IN','Indiana'),
        ('MI','Michigan'),
        ('WI','Wisconsin'),
    )
    regions = models.CharField(
        choices=REGIONS,
        max_length=250,
        default="IL",
        blank=True,
        null=True,
    )
    postal_code = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    COUNTRIES = (
        ('CA','Canada'),
        ('FR','France'),
        ('MX','Mexico'),
        ('US','United States'),
    )
    countries = models.CharField(
        choices=COUNTRIES,
        max_length=250,
        default="US",
        blank=True,
        null=True,
    )

    # def __str__(self):
    #     pass


class Source(Base):
    value = pg.JSONField()

    def __str__(self):
        return value

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def clean(self):
        # Make sure properties validate correctly.
        schema = source_schema

        v = Validator(schema)
        if not v.validate(self.value):
            raise ValidationError(
                {'properties': 'Properties do not fit schema for source.  Errors: {}'\
                .format(v.errors)})


TIMESPACE_LABELS = (
    ('born','born'),
    ('died','died'),
    ('started','started'),
    ('ended','ended'),
    ('lived','lived'),
    ('performed','performed'),
    ('occurred','occurred'),
    ('created','created'),
)

class RecordDate(Base):
    label = models.CharField(
        max_length=25,
        choices=TIMESPACE_LABELS,
    )
    record = models.ForeignKey('Record')
    date = models.ForeignKey('Date')


class RecordLocation(Base):
    label = models.CharField(
        max_length=25,
        choices=TIMESPACE_LABELS,
    )
    record = models.ForeignKey('Record')
    location = models.ForeignKey('Location')


class RecordSource(Base):
    accessed = models.DateField()
    record = models.ForeignKey('Record')
    source = models.ForeignKey('Source')


class Relation(Base):

    PREDICATES =  TIMESPACE_LABELS + (
        # item-level
            # relations flow in this direction, when possible
                # Event
                # Work
                # Organization
                # Person

            # event
            # (('has_event'), ('has event')), # reverse

            # work
            # (('has_work'), ('has work')), # reverse

            # person/organization
            ('has_contributor', 'has contributor'),
            ('has_creator', 'has creator'),
            ('has_curator', 'has curator'),
            ('has_editor', 'has editor'),
            ('has_employee', 'has employee'),
            ('has_exhibitor', 'has exhibitor'),
            ('has_friend', 'has friend'),
            ('has_member', 'has member'),
            ('has_organizer', 'has organizer'),
            ('has_owner', 'has owner'),
            ('has_parent', 'has parent'),
            ('has_producer', 'has producer'),
            ('has_publisher', 'has publisher'),
            ('has_affiliation', 'has affiliation'),
            ('has_spouse', 'has spouse'),
            ('has_translator', 'has translator'),
            ('has_venue', 'has_venue'),

            # generic
            ('part_of', 'part of'),
            ('same_as', 'same as'),

            # meta
            ('has_record_parent', 'has record parent'),
    )

    subject = models.ForeignKey('Record',
        related_name='relation_subject',
        on_delete=models.CASCADE,
    )
    predicate = models.CharField(
        choices=PREDICATES,
        max_length=25,
    )
    dobject = models.ForeignKey('Record',
        related_name='relation_direct_object',
        on_delete=models.CASCADE,
    )
    # properties = pg.JSONField(
    #     blank=True,
    #     null=True
    # )

    dates = models.ManyToManyField('Date')
    locations = models.ManyToManyField('Location')
    sources = models.ManyToManyField('Source')

    def __str__(self):
        return '( {} )-[ {} ]->( {} )'.format(self.subject, self.predicate, self.dobject)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def clean(self):
        # Make sure properties validate correctly.
        if self.predicate == 'has_record_source':
            schema = reference_schema
        else:
            schema = relation_schema

        if self.properties:
            v = Validator(schema)
            if not v.validate(self.properties):
                raise ValidationError(
                    {'properties': 'Properties do not fit schema for predicate {}.  Errors: {}'\
                    .format(self.predicate, v.errors)})


class Record(Base):
    class Meta:
        ordering = [
            '-created_on',
        ]

    schema = 'http://schema.org/Thing'

    LABELS = (
        ('event', 'event'),
        ('work', 'work'),
        ('person', 'person'),
        ('organization', 'organization'),
    )

    related = models.ManyToManyField('self',
        through='Relation',
        through_fields=('subject', 'dobject'),
        symmetrical=False,
        blank=True
    )
    name = models.CharField(
        max_length=250,
    )
    slug = models.SlugField(
        unique=True,
    )
    label = models.CharField(
        max_length=25,
        choices=LABELS,
    )
    properties = pg.JSONField()

    description = models.TextField(
        blank=True,
        null=True,
    )

    dates = models.ManyToManyField('Date',
        through='RecordDate',
    )
    locations = models.ManyToManyField('Location',
        through='RecordLocation',
    )
    sources = models.ManyToManyField('Source',
        through='RecordSource',
    )

    terms = models.ManyToManyField('Term',
        blank=True,
    )

    images = models.ManyToManyField('Image',
        blank=True,
    )

    is_active = models.NullBooleanField(
        default=True,
    )
    is_featured = models.BooleanField(
        default=False,
    )
    is_approved = models.BooleanField(
        default=True,
    )
    is_web_public = models.BooleanField(
        default=True,
    )

    # methods
    def __str__(self):
        return '{}/{}: {}'.format(self.label, self.types(), self.name)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def clean(self):
        # Make sure properties validate correctly.
        schemas = {
            'event': event_schema,
            'work': work_schema,
            'person': person_schema,
            'organization': organization_schema,
        }
        schema = schemas[self.label]
        if self.properties:
            v = Validator(schema)
            if not v.validate(self.properties):
                raise ValidationError(
                    {'properties': 'Properties do not fit {} schema.  Errors: {}'\
                    .format(self.label, v.errors)})

    def types(self):
        return '/'.join(self.properties['types'])

    def age(self):
        pass

    def citation(self):
        pass

    def date(self):
        pass

    def get_absolute_url(self):
        pass

    def location(self):
        pass

    def address(self):
        pass

    def distance(self):
        pass

    def duration(self): # lifespan
        pass

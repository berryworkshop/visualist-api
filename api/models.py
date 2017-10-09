from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres import fields as pg
from django.utils.timezone import now
from cerberus import Validator
import schemas


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


class Snippet(Base):
    value = models.TextField()
    source = models.ForeignKey('Source',
        blank=True,
        null=True,
    )
    source_url = models.URLField(
        blank=True,
        null=True
    )
    # source_pages = models.CharField(
    #     max_length=250,
    #     blank=True,
    #     null=True
    # )


    def __str__(self):
        if len(self.value) > 50:
            return self.value[:50] + '...'
        return self.value


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
    description = models.ForeignKey('Snippet',
        blank=True,
        null=True,
    )
    canonical_url = models.URLField(
        blank=True,
        null=True,
    )
    # parent = models.ForeignKey('self',
    #     related_name='children',
    #     blank=True,
    #     null=True,
    # )
    # same_as = models.ManyToManyField('self',
    #     blank=True,
    # )

    def __str__(self):
        if self.vocabulary:
            vocab = self.vocabulary.upper() + ': '
        else:
            vocab = ''
        return '{}{}'.format(vocab, self.value)


class Date(Base):
    class Meta:
        unique_together = (
            ("date", "duration", 'precision'),
        )

    date = models.DateTimeField()
    duration = models.PositiveIntegerField(
        # https://goo.gl/vA8HD8
        default=0
    )
    precision = models.PositiveIntegerField(
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
    region = models.CharField(
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

    def __str__(self):
        street_single_line = self.street.replace('\r\n', ', ')
        return '{}, {} {}'.format(street_single_line, self.locality, self.region)


class Source(Base):
    LABELS = (
        ('book','book'),
        ('website','website'),
        ('journal_article','journal article'),
        ('newspaper_article','newspaper article'),
    )
    label = models.CharField(
        max_length=25,
        choices=LABELS,
    )
    title = models.CharField(
        max_length=250
    )
    publisher = models.CharField(
        max_length=250,
        blank=True
    )
    place = models.CharField(
        max_length=250,
        blank=True
    )
    date = models.CharField(
        max_length=250,
        blank=True
    )
    base_url = models.URLField(
        max_length=250,
        blank=True,
    )
    # properties = pg.JSONField(
    #     default=dict(),
    #     blank=True,
    # )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    # def clean(self):
    #     # Make sure properties validate correctly.
    #     schema = schemas.source_schema

    #     v = Validator(schema)
    #     if self.properties and not v.validate(self.properties):
    #         raise ValidationError(
    #             {'properties': 'Extra properties do not fit schema for Source.  Errors: {}'\
    #             .format(v.errors)})


# class RecordSource(Base):
#     class Meta:
#         unique_together = (
#             ('record','source'),
#         )

#     accessed = models.DateField(
#         default = now
#     )
#     record = models.ForeignKey('Record')
#     source = models.ForeignKey('Source')

#     # properties = pg.JSONField(
#     #     default=dict(),
#     #     blank=True,
#     # )

#     def __str__(self):
#         return '{} --> {}'.format(self.record, self.source)

#     def save(self, *args, **kwargs):
#         self.full_clean()
#         return super().save(*args, **kwargs)

#     # def clean(self):
#     #     # Make sure properties validate correctly.
#     #     schema = schemas.record_source_schema

#     #     v = Validator(schema)
#     #     if self.properties and not v.validate(self.properties):
#     #         raise ValidationError(
#     #             {'properties': 'Extra properties do not fit schema for Source.  Errors: {}'\
#     #             .format(v.errors)})


class Relation(Base):

    PREDICATES = (
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
            ('has_affiliation', 'affiliated with'),
            ('has_contributor', 'has contributor'),
            ('has_creator', 'has creator'),
            ('has_curator', 'has curator'),
            ('has_date', 'has date'),
            ('has_editor', 'has editor'),
            ('has_employee', 'has employee'),
            ('has_exhibitor', 'has exhibitor'),
            ('has_existence', 'exists'),
            ('has_friend', 'has friend'),
            ('has_life', 'is alive'),
            ('has_location', 'has location (NOT venue)'),
            ('has_member', 'has member'),
            ('has_organizer', 'has organizer'),
            ('has_owner', 'has owner'),
            ('has_parent', 'has parent'),
            ('has_performer','has performer'),
            ('has_primary', 'is a subsidiary of'),
            ('has_producer', 'has producer'),
            ('has_publisher', 'has publisher'),
            ('has_spouse', 'is married to'),
            ('has_translator', 'has translator'),
            ('has_venue', 'has venue'),

            # generic
            ('part_of', 'part of'),
            ('same_as', 'same as'),
    )

    subject = models.ForeignKey('Record',
        on_delete=models.CASCADE,
    )
    predicate = models.CharField(
        choices=PREDICATES,
        max_length=25,
    )
    dobject = models.ForeignKey('Record',
        related_name='reverse_relations',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    # properties = pg.JSONField(
    #     default={},
    #     blank=True,
    #     null=True,
    # )

    dates = models.ManyToManyField('Date',
        blank=True,
    )
    locations = models.ManyToManyField('Location',
        blank=True,
    )

    source = models.ForeignKey('Source',
        blank=True,
        null=True,
    )

    def __str__(self):
        s = '( {} )-[ {} ]'.format(self.subject, self.predicate)
        if self.dobject:
            s = s + '->( {} )'.format(self.dobject)
        return s

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    # def clean(self):
    #     # Make sure properties validate correctly.
    #     if self.predicate == 'has_record_source':
    #         schema = schemas.reference_schema
    #     else:
    #         schema = schemas.relation_schema

    #     if self.properties:
    #         v = Validator(schema)
    #         if not v.validate(self.properties):
    #             raise ValidationError(
    #                 {'properties': 'Properties do not fit schema for predicate {}.  Errors: {}'\
    #                 .format(self.predicate, v.errors)})


class Record(Base):
    class Meta:
        ordering = [
            '-created_on',
        ]

    schema = 'http://schema.org/Thing'

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

    LABELS = (
        ('event', 'event'),
        ('work', 'work'),
        ('person', 'person'),
        ('organization', 'organization'),
    )
    SUBLABELS = {
        'event': [
            'course',
            'convention',
            'exhibition',
            'fair',
            'performance',
            'reception',
            'residency',
            'workshop',
        ],
        'work': [
            'article',
            'artwork',
            'book',
            'installation',
            'license',
            'photograph',
            'sculpture',
            'vocabulary',
            'website',
        ],
        'person': [
            'architect',
            'artist',
            'curator',
            'filmmaker',
            'gallerist',
            'manager',
            'professor',
            'programmer',
            'writer',
        ],
        'organization': [
            'archive',
            'association',
            'company',
            'consortium',
            'foundation',
            'gallery',
            'library',
            'museum',
            'publisher',
            'school',
        ],
        # 'page': [
        #     'article',
        #     'collection',
        #     'post',
        #     'review',
        #     'tour',
        # ]
    }
    label = models.CharField(
        max_length=25,
        choices=LABELS,
    )
    sublabels = pg.ArrayField(
        models.CharField(max_length=25)
    )

    # properties = pg.JSONField(
    #     blank=True,
    #     default=dict()
    # )
    description = models.ForeignKey('Snippet',
        blank=True,
        null=True,
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

    is_primary = models.BooleanField(
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
        sublabels = '/'.join(self.sublabels)
        return '{}/{}: {}'.format(self.label, sublabels, self.name)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def clean(self):
        if self.sublabels:
            for sublabel in self.sublabels:
                if sublabel not in Record.SUBLABELS[self.label]:
                    raise ValidationError(
                        {'sublabels': 'Sublabels do not fit {} label.  Choices are: {}'\
                        .format(self.label, Record.SUBLABELS[self.label])})
        else:
            raise ValidationError(
                {'sublabels': 'Please select at least one sublabel.  Choices are: {}'\
                .format(Record.SUBLABELS[self.label])})

        # Make sure properties validate correctly.
        # record_schemas = {
        #     'event': schemas.event_schema,
        #     'work': schemas.work_schema,
        #     'person': schemas.person_schema,
        #     'organization': schemas.organization_schema,
        # }
        # schema = record_schemas[self.label]
        # if self.properties:
        #     v = Validator(schema)
        #     if not v.validate(self.properties):
        #         raise ValidationError(
        #             {'properties': 'Properties do not fit {} schema.  Errors: {}'\
        #             .format(self.label, v.errors)})


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

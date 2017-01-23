from django.db import models
from .base import Base, Record
from django.core.validators import MaxValueValidator
# from .joins import BodyPlaceJoin
# from .space import Place

class Body(Record):
    '''
    A person or organization.
    '''

    TYPES = (
        ('PERSON','person'),
        ('ARCHIVE', 'archive'),
        ('ASSOCIATION', 'association'),
        ('COMPANY', 'company'),
        ('ENSEMBLE', 'ensemble'),
        ('FOUNDATION', 'foundation'),
        ('GALLERY', 'gallery'),
        ('LIBRARY', 'library'),
        ('MUSEUM', 'museum'),
        ('SCHOOL', 'school'),
    )
    body_types = models.CharField(max_length=20,
        choices=TYPES,
        default="PERSON")

    first_name = models.CharField(max_length=100, blank=True)

    # TODO
    # date_birth = ApproximateDateField()
    # date_death = ApproximateDateField()

    body_parents = models.ManyToManyField('self',
        symmetrical=False,
        blank=True,
        through="Relationship",
        through_fields=('parent', 'child'))

    places = models.ManyToManyField('Place', blank=True,
        through='BodyPlaceJoin')

    def __str__(self):
        return self.name


class Relationship(models.Model):
    parent = models.ForeignKey('Body', on_delete=models.CASCADE,
        related_name="children")
    child = models.ForeignKey('Body', on_delete=models.CASCADE,
        related_name="parents")
    RELATIONS = (
        ('MEMBER','is member of'),
        ('FRIEND','is friend of'),
    )
    relation_type = models.CharField(max_length=25, 
        choices=RELATIONS, default='MEMBER')


class Alias(Base):
    '''An alternate name for a place or organization'''
    body = models.ForeignKey('Body', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)


class ContactItem(Base):
    '''A superclass for shared functionality between body line-items.'''

    class Meta:
        abstract = True

    TYPES = (
        ('BUSINESS','business'), 
        ('PERSONAL','personal'), 
    )

    body = models.ForeignKey('Body',
        on_delete=models.CASCADE,
        related_name="%(class)s_set")
    contact_item_type = models.CharField(max_length=20,
        choices=TYPES, default="PERSONAL")


class Account(ContactItem):
    '''A social media account'''
    
    SERVICES = (
        ('FACEBOOK', 'Facebook'),
        ('PINTEREST', 'Pinterest'),
        ('TUMBLR', 'Tumblr'),
        ('TWITTER', 'Twitter'),
    )

    service = models.CharField(max_length=20,
        choices=SERVICES, default="FACEBOOK")
    username = models.CharField(max_length=100)

    def __str__(self):
        return "{}: {}".format(self.service, self.username)


# class Address(ContactItem):
#     '''A street address.'''

#     pass


class Email(ContactItem):
    '''An email address.'''
    
    email_address = models.EmailField()

    def __str__(self):
        return self.email_address


class Phone(ContactItem):
    '''A phone number.'''
    
    country_code = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(999)],
        default=1)
    area_code = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(999)])
    number = models.PositiveIntegerField(
        validators=[MaxValueValidator(9999999)])

    def __str__(self):
        number = "{}-{}".format(str(self.number)[:3], str(self.number)[3:])
        return "+{} ({}) {}".format(self.country_code, self.area_code, number)


class Website(ContactItem):
    '''The highest-level relevant URL for a website.'''
    
    url = models.URLField()

    def __str__(self):
        return self.url


# maybe best for following to use an existing Django solution from PyPI
# class HourSet(Base):
#     '''A defined set of operating hours.'''
    
#     name = models.CharField(max_length=250)

#     start_date = models.DateField(blank=True, null=True)
#     end_date = models.DateField(blank=True, null=True)


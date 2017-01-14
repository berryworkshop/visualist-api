from django.db import models
from cms.models import Record, Base
from .countries import COUNTRIES
from django.core.validators import MaxValueValidator

class Contact(Record):
    '''
    Superclass for shared functionality between Person and Organization.
    This uses multi-table inheritance, so be careful with adjustments.
    '''
    pass




class Person(Contact):
    '''A human being.'''

    class Meta:
        verbose_name_plural = 'people'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Organization(Contact):
    '''An organized group of humans.'''

    name = models.CharField(max_length=255)

    TYPES = (
       ('ARCHIVE', 'archive'),
       ('ASSOCIATION', 'association'),
       ('COMPANY', 'company'),
       ('CONSORTIUM', 'consortium'),
       ('FOUNDATION', 'foundation'),
       ('GALLERY', 'gallery'),
       ('LIBRARY', 'library'),
       ('MUSEUM', 'museum'),
       ('SCHOOL', 'school'),
    )

    organization_types = models.CharField(max_length=20,
        choices=TYPES,
        blank=False,
        default="ASSOCIATION")

    def __str__(self):
        return self.name


class ContactItem(Base):
    '''A superclass for shared functionality between contact line-items.'''

    class Meta:
        abstract = True

    TYPES = (
        ('BUSINESS','business'), 
        ('PERSONAL','personal'), 
    )

    contact = models.ForeignKey('Contact',
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
    username = models.CharField(max_length=255)

    def __str__(self):
        return "{}: {}".format(self.service, self.username)


class Address(ContactItem):
    '''A street address.'''

    class Meta:
        verbose_name_plural = "addresses"

    street = models.TextField()
    city = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255,
        choices=COUNTRIES,
        default="USA")

    def __str__(self):
        streets = [s.strip() for s in self.street.split('\n')]
        street = ', '.join(streets)
        return "{}, {}, {}, {}, {}".format(street, self.city,
            self.state_province, self.postal_code, self.country)


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
    
#     name = models.CharField(max_length=255)

#     start_date = models.DateField(blank=True, null=True)
#     end_date = models.DateField(blank=True, null=True)


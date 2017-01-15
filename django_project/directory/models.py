from django.db import models
from base.models import Base, Record
from django.core.validators import MaxValueValidator


class Contact(Record):
    '''
    The abstract superclass for People and Organizations,
    or other relevant future Record types.
    '''
    synopsis = models.TextField(max_length=250, blank=True, null=True)


class Person(Contact):
    '''A human being.'''

    class Meta:
        verbose_name_plural = 'people'

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)

    def name(self):
        return "{}, {}".format(self.last_name, self.first_name)

    def __str__(self):
        return self.name()


class Organization(Contact):
    '''An organized group of humans.'''

    name = models.CharField(max_length=100)

    TYPES = (
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


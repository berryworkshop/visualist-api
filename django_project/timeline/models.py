from django.db import models
from django.urls import reverse
from cms.models import Record, Term


class Event(Record):
    '''A named art event, performance or happening.'''

    name = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField()

    datetime_start = models.DateTimeField(blank=False, null=False)
    datetime_end = models.DateTimeField(blank=True, null=True)

    TYPES = [
        "event",
        "performance",
    ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event', args=[self.pk])


class Period(Term):
    '''
    A named span of time, e.g. an epoch, era, or an art historical movement.
    '''
    pass


# Event
#     date start
#     date end
#     Receptions
#     names
#     Venue -> org
#     Facebook links
#     weblinks
#     picture
#         largely limited to a single postcard-esque image per show
#         multiples possible
# Event
#     Import
#         Google
#         iCal
#         Yahoo
#         Facebook
#         Outlook
#     Suitable for
#         All Ages
#         Adults
#         Babies
#         Kids
#         Preschoolers
#         Seniors
#         Teens
#         Toddlers
#     Custom fields
#         ApproxDateField
#         TimeSpanField
# Kind of Event
#         Exhibition
#             Opening Date
#             Closing Date
#             Reception Date
#             Reception Time
#             description
#             Image
#             Facebook link
#         Reading
#             Date(s)
#             Time
#             Description
#             Image
#             Facebook link
#         Lecture/Panel/Artist Talk
#             Date(s)
#             Time
#             Description
#             Image
#             Facebook link
#         Performance
#             Date(s)
#             Time
#             Description
#             Image
#             Facebook link
#     Are there other programs associated with this event (y/n)
#         If yes
#         How many? (Adds the amount of drop downs needed)
#         Title
#         Date
#         Time
#         Kind of Event
#             Exhibition
#             Reading
#             Lecture
#             Performance
#         Facebook link
#         Description
#         Is this event on-site (y/n)
#     If not
#         Venue
#         Address
#         City, State, Zip
#         Phone 
#         Email
#         Web
#         For internal use only
#             Contact name
#             Contact email
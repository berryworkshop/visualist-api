from django.db import models
from .base import Base, Record
# from thesaurus.models import Term
from django.urls import reverse
from django.utils.timezone import now
# from .space import Place
# from .people import Body
# from .joins import EventPlaceJoin, BodyEventJoin


class Event(Record):
    '''
    A span on a timeline with a beginning and end.
    '''

    #
    # Base fields
    # # #

    TYPES = (
        ("EXHIBITION", "exhibition"),
        ("PERFORMANCE", "performance"),
        ("WORKSHOP", "workshop"),
    )
    record_type = models.CharField(max_length=20,
        choices=TYPES,
        default="EXHIBITION")

    start = models.DateTimeField(blank=False, null=False, default=now)
    end = models.DateTimeField(blank=True, null=True, default=now)

    places = models.ManyToManyField('Place', blank=True,
        through='EventPlaceJoin')
    bodies = models.ManyToManyField('Body', blank=True,
        through='BodyEventJoin')

    def __str__(self):
        return name

    def get_absolute_url(self):
        return reverse('event', args=[self.pk])

    #
    # Exhibition Fields
    # # #

    #
    # Performance Fields
    # # #

    #
    # Workshop Fields
    # # #

    


# class Reminder(Record):
#     pass


# --------------------------------- #
# following are just brainstorms

    # AUDIENCES = [
    #     'for all ages', 
    #     'young children: 0-5',
    #     'children: 5-10',
    #     'young adult',
    #     'primarily for adults',
    #     'adults only',
    # ]

# Event
#     date start
#     date end
#     Receptions
#     names
#     Place -> org
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
#         Place
#         Address
#         City, State, Zip
#         Phone 
#         Email
#         Web
#         For internal use only
#             Body name
#             Body email

# class Event(Base):
   # when = models.DateTimeField()
   # duration = models.IntegerField()
   # place = models.ForeignKey('Organization', models.SET_NULL)
  # not sure about these ones
   # on_site = models.BooleanField(default=True)
   # body_name = ...
   # body_email = ...
  # EVENT_TYPES = (
       # ('EXHIBITION', 'exhibition'),
       # ('READING', 'reading'),
       # ('TALK', 'talk'),
       # ('LECTURE', 'lecture'),
       # ('PANEL', 'panel'),
       # ('PERFORMANCE', 'performance'),
       # ('OPENING', 'opening reception'),
       # ('CLOSING', 'closing reception'),
       # )
   # event_type = models.CharField(max_length=15, choices=EVENT_TYPES)
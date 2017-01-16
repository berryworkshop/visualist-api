from django.db import models
from django.utils.timezone import now


class Source(models.Model):
    '''
    The object of a citation, e.g. an item of media, 
    a location on the internet, a book, a speech, or a conversation.
    '''
    created = models.DateTimeField(default=now)
    modified = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    URL = models.URLField()
    version = models.CharField(max_length=250)
    checked = models.DateField()

    TYPES = (
        ('WEBSITE', 'website'),
        ('BOOK', 'book'),
        ('ARCHIVE', 'archive'),
    )
    source_type = models.CharField(max_length=250, choices=TYPES)
    notes = models.TextField()

    def populate_from_url(self):
        # TODO
        pass

    def populate_from_previous(self):
        # TODO
        pass

    def cite_mla(self):
        # TODO
        pass

    def cite_chicago(self):
        # TODO
        pass



# class RightSet(Base):
#     '''A set of rules defining copyright for a Record.'''
#     pass


# class Service(Term):
#     '''An online or social media service.'''
#     pass

# - - - - - - - - - - - - - - - - - - - - - - - - #

# round-trip
    # iCal


# import
    # iCal
# export
    #ical
# controlled vocabularies
    # Getty AAT
    # Getty TGN
    # LoC Subjects
    # Getty ULAN


def query_getty_aat(query):
    pass

def query_getty_tgn(query):
    pass

def query_getty_ulan(query):
    pass

def query_loc_subjects(query):
    pass
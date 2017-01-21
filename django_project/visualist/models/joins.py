from django.db import models
from django.utils.timezone import now
# from .people import Contact
# from .space import Venue
# from .things import Work
# from .time import Event

# This set of classes isn't really for direct use, but through subclasses.
# Should not have views, for example.


class EventVenueJoin(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE)
    RELATIONS = (
        ('HOSTED','hosted at'),
    )
    relation_type = models.CharField(max_length=25,
        choices=RELATIONS, default='SHOWN')


class ContactEventJoin(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    RELATIONS = (
        ('PRODUCED','producer of'),
        ('HOSTED','host of'),
        ('SHOWN','shown work during'),
    )
    relation_type = models.CharField(max_length=25,
        choices=RELATIONS, default='PRODUCED')


class ContactVenueJoin(models.Model):
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE)
    RELATIONS = (
        ('OCCUPIED','occupant of'),
        ('OWNER','owner of'),
    )
    relation_type = models.CharField(max_length=25,
        choices=RELATIONS, default='OCCUPIED')


class WorkContactJoin(models.Model):
    work = models.ForeignKey('Work', on_delete=models.CASCADE)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    RELATIONS = (
        ('CREATED','created by'),
        ('PUBLISHED','published by'),
        ('OWNED', 'owned by'),
        ('COLLECTION', 'in the collection of'),
    )
    relation_type = models.CharField(max_length=25, 
        choices=RELATIONS, default='CREATED')


class WorkEventJoin(models.Model):
    work = models.ForeignKey('Work', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    RELATIONS = (
        ('SHOWN','shown during'),
    )
    relation_type = models.CharField(max_length=25,
        choices=RELATIONS, default='SHOWN')


class WorkVenueJoin(models.Model):
    work = models.ForeignKey('Work', on_delete=models.CASCADE)
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE)
    RELATIONS = (
        ('SHOWN','shown at'),
    )
    relation_type = models.CharField(max_length=25,
        choices=RELATIONS, default='SHOWN')
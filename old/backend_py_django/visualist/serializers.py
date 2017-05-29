from .models import Body, Event, Place, Work
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


record_fields = (
    'id',
    'name',
    'slug',
    'created',
    'modified',
    'description',
    # 'record_type',
    'get_absolute_url',
)


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = record_fields


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = record_fields + (
            'hours_open',
            'appointment_only',
        )


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Work
        fields = record_fields


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Body
        fields = record_fields


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Body
        fields = record_fields
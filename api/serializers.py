from django.contrib.auth.models import User, Group
from .models import Record, Relation
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ('url', 'slug', 'label', 'name',
            # 'description',
            'relations_by_subject'
        )


class RelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relation
        fields = ('subject', 'predicate', 'dobject')

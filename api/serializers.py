from django.contrib.auth.models import User, Group
from .models import Snippet, Record, Relation
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('pk', 'url', 'name')


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            # 'pk',
            'value', 'source_url',
            # 'source'
        )


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = (
            # 'pk',
            'url',
            'slug', 'label', 'name', 'sublabels',
            'description',
            # 'relations'
        )

    description = SnippetSerializer()

    def create(self, validated_data):
        return Record.objects.create(**validated_data)



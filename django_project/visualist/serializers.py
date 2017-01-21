from .models import Event
from rest_framework import serializers

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('created', 'modified', 'name', 'description', 
            'datetime_start', 'datetime_end', 'get_absolute_url')
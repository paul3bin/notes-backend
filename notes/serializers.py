from rest_framework import serializers

from . import models


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notes
        fields = '__all__'
        read_only_fields = ('created_on', 'last_updated')

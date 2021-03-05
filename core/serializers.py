from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%a, %d. %b %Y ob %H:%M", required=False, read_only=True)
    
    class Meta:
        model = Story
        fields = ('__all__')
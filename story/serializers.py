from rest_framework import serializers
from .models import Story,Comment

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        exclude = []

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = []
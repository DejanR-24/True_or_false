from django import forms
from .models import Story,Comment

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = [
            'text',
            'ans',
            'author',
        ]
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
            'author',
            'story'
        ]
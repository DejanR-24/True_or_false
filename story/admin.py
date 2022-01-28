from django.contrib import admin
from .models import Story,Comment

class StoryAdmin(admin.ModelAdmin):
    list_display=('text','author',)

class CommentAdmin(admin.ModelAdmin):
    list_display=('text','author','story_id')

admin.site.register(Story,StoryAdmin)
admin.site.register(Comment,CommentAdmin)


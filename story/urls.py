from django.urls import path
from . import views

urlpatterns=[
    path('stories/',views.stories,name='all-stories'),
    path('stories/<int:story_ID>/',views.story_comments,name='story-comments'),
    path('my_stories/',views.my_stories,name='my-stories'),
    path('add_story/',views.add_story,name='add_story'),

]
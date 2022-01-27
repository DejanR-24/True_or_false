from django.urls import path
from . import views

urlpatterns=[
    #path('stories/',views.stories,name='all-stories'),
    #path('stories/<int:story_ID>/',views.story_comments,name='story-comments'),
    path('my_stories/',views.my_stories,name='my-stories'),
    path('add_story/',views.add_story,name='add_story'),
    path("",views.Home.as_view(),name="home"),
    #path('stories/<int:story_ID>/',views.StoryComments.as_view(),name="story-comments"),
    path('stories/<int:pk>/',views.StoryDetail.as_view(),name="story-comments"),
    path('dashboard/',views.Dashboard.as_view(),name='dashboard'),
    path('stories/<int:pk>/update/',views.StoryUpdate.as_view(),name='update_story'),
    path('stories/<int:pk>/delete/',views.StoryDelete.as_view(),name='delete_story'),

]
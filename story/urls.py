from django.urls import path
from . import views

urlpatterns=[

    path("",views.Home.as_view(),name="home"),
    path('my_stories/',views.MyStories.as_view(),name='my_stories'),
    path('story/<int:pk>/',views.StoryDetail.as_view(),name="story_comments"),
    path('dashboard/',views.Dashboard.as_view(),name='dashboard'),
    path('story/add/',views.AddStory.as_view(),name='add_story'),
    path('story/<int:pk>/update/',views.StoryUpdate.as_view(),name='update_story'),
    path('story/<int:pk>/delete/',views.StoryDelete.as_view(),name='delete_story'),


]   
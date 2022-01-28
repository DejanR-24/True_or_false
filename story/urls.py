from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_view

from . import views


urlpatterns=[
    path("login/",auth_view.LoginView.as_view(template_name="story/login.html"),name="login"),
    path("logout/",auth_view.LogoutView.as_view(),name="logout"),
    path("",views.Home.as_view(),name="home"),
    path('my_stories/',views.MyStories.as_view(),name='my_stories'),
    path('story/<int:pk>/',views.StoryDetail.as_view(),name="story_detail"),
    path('dashboard/',views.Dashboard.as_view(),name='dashboard'),
    path('story/add/',views.AddStory.as_view(),name='add_story'),
    path('story/<int:pk>/update/',views.StoryUpdate.as_view(),name='update_story'),
    path('story/<int:pk>/delete/',views.StoryDelete.as_view(),name='delete_story'),
    path('story/<int:pk>/true',views.true_story,name='true_story'),
    path('story/<int:pk>/false',views.false_story,name='false_story'),

]   
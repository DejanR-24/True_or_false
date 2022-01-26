
from django.db.models.fields.related import ForeignKey
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import View
from .models import Story,Comment
from .forms import StoryForm,CommentForm




def stories(request):
    all_stories = Story.objects.all() #SELECT * FROM OBJAVE
    return render(request, 'story/stories.html',{'stories':all_stories})

def story_comments(request,story_ID):
    comments = Comment.objects.filter(story_id=story_ID)   #story=story.objects.get(id=story_ID)) #SELECT * FROM KOMENTARI WHERE OBJAVE_ID=
    story = Story.objects.get(id=story_ID)
    username = request.user.username
    initial_data ={
        'story': story_ID,
        'author': username,
    }
    form=CommentForm(request.POST or None,initial=initial_data)
    if form.is_valid():
        form.save()
    return render(request, 'story/comments.html',{'story':story,'comments':comments, 'form':form})

def my_stories(request):
    username = request.user.username
    only_my_stories = Story.objects.filter(author=username) #SELECT * FROM OBJAVE WHERE USERNAME=User.username
    return render(request, 'story/my_stories.html',{'my_stories': only_my_stories})

def add_story(request):
    if request.method == 'POST':
        text= request.POST["text"]
        ans= True if request.POST["ans"]=='on' else False
        author = request.user
        Story.objects.create(text = text, ans = ans, author = author).save()
        return redirect('/my_stories')
    else:
        return render(request, 'story/add_story.html')



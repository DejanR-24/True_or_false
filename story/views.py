from django.db.models.fields.related import ForeignKey
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.views.generic import View,ListView,UpdateView,CreateView,DetailView,FormView,DeleteView
from .models import Story,Comment
from .forms import StoryForm,CommentForm
from django.urls import reverse_lazy


#class Home(View):
#    def get(self,request):
 #       all_stories =  Story.objects.all() 
  #      return render(request, 'story/stories.html',{'stories':all_stories})

class Home(ListView):
    model = Story
    context_object_name = 'stories'
    queryset = Story.objects.all()
    template_name = 'story/stories.html'
    ordering = '-id'
    paginate_by = '10'


class StoryDisplay(DetailView):
    model = Story
    context_object_name = 'story'
    def get_object(self):
        object= super(StoryDisplay,self).get_object()
        object.save()
        return object

    def get_context_data(self,**kwargs):
        context = super(StoryDisplay,self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(story=self.get_object())
        context['form'] = CommentForm
        return context

class StoryComment(FormView):
    form_class = CommentForm
    template_name = 'story/comments.html'

    def form_valid(self,form):
        form.instance.author= self.request.user
        story = Story.objects.get(pk=self.kwargs['pk'])
        form.instance.story = story
        form.save()
        return super(StoryComment,self).form_valid(form)
    
    def get_success_url(self):
        return reverse('story_comments',kwarg={'pk':self.kwargs['pk']})

class StoryDetail(View):
    def get(self,request,*args, **kwargs):
        view = StoryDisplay.as_view(
            template_name = 'story/comments.html'
        )
        return view(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        view = StoryComment.as_view(
            template_name = 'story/comments.html'
        )
        return view(request,*args, **kwargs)

'''
class StoryComment(ListView):
    def get(self,request,story_ID):
        story = Story.objects.get(id=story_ID)
        comments = Comment.objects.filter(story_id=story_ID)
        return render(request, 'story/comments.html',{'story':story,'comments':comments})
    model = Comment
    context_object_name = 'comments'
    queryset = Comment.objects.filter(story_id=story_ID)
    template_name = 'story/stories.html'
    ordering = '-id'
    paginate_by = '10'
    
    def post(self,request,story_ID):
        form=CommentForm(request.POST or None)
        if form.is_valid():
            form.save()
        story = Story.objects.get(id=story_ID)
        comments = Comment.objects.filter(story_id=story_ID)
        return render(request, 'story/comments.html',{'story':story,'comments':comments,'form':form})

class StoryComment(View):
    def get(self,request,story_ID):
        story = Story.objects.get(id=story_ID)
        comments = Comment.objects.filter(story_id=story_ID)
        return render(request, 'story/comments.html',{'story':story,'comments':comments})
    
    def post(self,request,story_ID):
        form=CommentForm(request.POST or None)
        if form.is_valid():
            form.save()
        story = Story.objects.get(id=story_ID)
        comments = Comment.objects.filter(story_id=story_ID)
        return render(request, 'story/comments.html',{'story':story,'comments':comments,'form':form})
'''
class Dashboard(View):
    def get(self,request,*args, **kwargs):
        view = Home.as_view(
            template_name = 'story/admin.html'
        )
        return view(request,*args, **kwargs)

class StoryUpdate(UpdateView):
    model = Story
    fields = ('text','ans')

class StoryDelete(DeleteView):
    model = Story
    success_url = reverse_lazy('dashboard')


class AjaxHandlerView(View):
            def get(self,request):
                text = request.GET.get("true_button")
                print()
                print(text)
                print()
                return render(request, 'story/stories.html')

def stories(request):
    all_stories = Story.objects.all() #SELECT * FROM OBJAVE
    return render(request, 'story/stories.html',{'stories':all_stories})

def story_comments(request,story_ID):
    comments = Comment.objects.filter(story_id=story_ID)   #story=story.objects.get(id=story_ID)) #SELECT * FROM KOMENTARI WHERE OBJAVE_ID=
    story = Story.objects.get(id=story_ID)
    form=CommentForm(request.POST or None)
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




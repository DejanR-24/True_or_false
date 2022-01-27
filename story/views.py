from django.db.models.fields.related import ForeignKey
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.views.generic import View,ListView,UpdateView,DetailView,FormView,DeleteView
from .models import Story,Comment
from .forms import StoryForm,CommentForm
from django.urls import reverse_lazy


'''class Home(View):
    def get(self,request):
        all_stories =  Story.objects.all() 
        return render(request, 'story/stories.html',{'stories':all_stories})
'''

class Home(ListView):
    model = Story
    context_object_name = 'stories'
    queryset = Story.objects.all()
    template_name = 'story/stories.html'
    ordering = '-id'
    paginate_by = '10'

class MyStories(ListView):
    model = Story
    context_object_name = 'my_stories'
    template_name = 'story/my_stories.html'
    ordering = '-id'
    paginate_by = '10'

    def get_queryset(self):
        return Story.objects.filter(author=self.request.user)


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
        return reverse_lazy('story_comments',kwarg={'pk':self.kwargs['pk']})

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


class Dashboard(View):
    def get(self,request,*args, **kwargs):
        view = Home.as_view(
            template_name = 'story/admin.html'
        )
        return view(request,*args, **kwargs)

class StoryUpdate(UpdateView):
    model = Story
    fields = ('text','ans')

    def get_success_url(self):
        return reverse_lazy('my_stories')

class StoryDelete(DeleteView):
    model = Story
    success_url = reverse_lazy('dashboard')

class AddStory(FormView):
    form_class = StoryForm
    template_name = 'story/story_form.html'

    def form_valid(self,form):
        form.instance.author= self.request.user
        form.save()
        return super(AddStory,self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('my_stories')

class AjaxHandlerView(View):
            def get(self,request):
                text = request.GET.get("true_button")
                print()
                print(text)
                print()
                return render(request, 'story/stories.html')


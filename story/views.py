from django.db.models.fields.related import ForeignKey
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import View,ListView,UpdateView,DetailView,FormView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse

from .models import Story,Comment
from .forms import StoryForm,CommentForm


class Home(ListView):
    model = Story
    context_object_name = 'stories'
    queryset = Story.objects.all()
    template_name = 'story/stories.html'
    paginate_by = '10'

@method_decorator(login_required,name='dispatch')
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
        this_story=super(StoryDisplay,self).get_object()
        total_true=this_story.total_t()
        total_false=this_story.total_f()       
        context['total_true']=total_true
        context['total_false']=total_false
        context['form'] = CommentForm
        return context

@method_decorator(login_required,name='dispatch')
class StoryComment(FormView):
    form_class = CommentForm
    template_name = 'story/story_detail.html'

    def form_valid(self,form):
        form.instance.author= self.request.user
        story = Story.objects.get(pk=self.kwargs['pk'])
        form.instance.story = story
        form.save()
        return super(StoryComment,self).form_valid(form)
    
    def get_success_url(self): 
        return reverse('story_detail',kwarg={'pk':self.kwargs['pk']})

class StoryDetail(View):
    def get(self,request,*args, **kwargs):  
        view = StoryDisplay.as_view(
            template_name = 'story/story_detail.html'
        )
        return view(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        view = StoryComment.as_view(
            template_name = 'story/story_detail.html'
        )
        return view(request,*args, **kwargs)

@method_decorator(login_required,name='dispatch')
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
    
@method_decorator(login_required,name='dispatch')
class AddStory(FormView):
    form_class = StoryForm
    template_name = 'story/story_form.html'

    def form_valid(self,form):
        form.instance.author= self.request.user
        form.save()
        return super(AddStory,self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('my_stories')

def true_story(request,pk):
    story = get_object_or_404(Story, id=request.POST.get('true_story_id'))
    story.t.add(request.user)
    return HttpResponseRedirect(reverse('story_detail', args=[str(pk)]))

def false_story(request,pk):
    story = get_object_or_404(Story, id=request.POST.get('false_story_id'))
    story.f.add(request.user)
    return HttpResponseRedirect(reverse('story_detail', args=[str(pk)]))

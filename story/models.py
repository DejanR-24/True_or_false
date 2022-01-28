from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import BooleanField, CharField, IntegerField, TextField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

class Story(models.Model):
    text = models.TextField(max_length=2000,unique=True,default='')
    t = models.ManyToManyField(User,related_name='vote_true')
    f = models.ManyToManyField(User,related_name='vote_false')
    ans = models.BooleanField(default=False)
    author = models.ForeignKey(User,to_field='username',on_delete=models.CASCADE)

    def total_t(self):
        return self.t.count()

    def total_f(self):
        return self.f.count()
    

    def __str__(self):
        return f'{self.text[:10]}... a napisao je {self.author}' 
    
    def __repr__(self):
        return 'Stories' 

class Comment(models.Model):
    text = models.CharField(max_length=550,unique=True,default='')
    story = models.ForeignKey(Story,on_delete=models.CASCADE) #       objava = models.ForeignKey("Objava",on_delete=models.DO_NOTHING) 
    author=models.ForeignKey(User, to_field='username',on_delete=models.CASCADE,default="")
    #author=ForeignKey(User,on_delete=models.DO_NOTHING,default="") uzima samo user_ids


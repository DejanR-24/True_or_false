from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import BooleanField, CharField, IntegerField, TextField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

class Story(models.Model):
    text=TextField(max_length=2000,unique=True,default='')
    t=IntegerField(default=0)
    f=IntegerField(default=0)
    ans=BooleanField(default=False)
    author=ForeignKey(User,to_field='username',on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.text[:10]}... a napisao je {self.author}' 

class Comment(models.Model):
    text=CharField(max_length=550,unique=True,default='')
    result=IntegerField(default=0)
    story = models.ForeignKey(Story,on_delete=models.CASCADE) #       objava = models.ForeignKey("Objava",on_delete=models.DO_NOTHING) 
    author=ForeignKey(User, to_field='username',on_delete=models.CASCADE,default="")
    #author=ForeignKey(User,on_delete=models.DO_NOTHING,default="") uzima samo user_id
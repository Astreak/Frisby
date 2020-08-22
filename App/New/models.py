from django.db import models
from django.contrib.auth.models import User
import datetime

class car(models.Model):
    Owner=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=1300,default="merc")
    color=models.CharField(max_length=1400,default="black")
    price=models.CharField(max_length=500)
    date=models.DateTimeField("Date",default=datetime.datetime.now())
    def __str__(self):
        return f"{self.Owner}";

class Question(models.Model):
    statement=models.CharField(max_length=1000)
    pub_date=models.DateTimeField("Date",default=datetime.datetime.now())

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE);
    ans=models.CharField(max_length=100)
    votes=models.IntegerField(default=0)
    author=models.OneToOneField(User,on_delete=models.CASCADE,default=1);

class Music(models.Model):
    G=(
        ("hip Hop","Hip Hop"),
        ("Pop","Pop"),
        ("classical","classical"),
        ("chill","chill")
    );
    genre=models.CharField(max_length=100,choices=G)
    subscriber=models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    song=models.CharField(max_length=200)
    urls=models.URLField(default="https://www.google.com")
    def __str__(self):
        return  f"{self.subscriber} songs"
    
class Msg(models.Model):
    sen=models.ForeignKey(User,on_delete=models.CASCADE,default=1,related_name='%(class)s_requests_created')
    rec=models.ForeignKey(User,on_delete=models.CASCADE,default=2)
    text=models.TextField()
    mdl=models.TextChoices("Hola","Hiya")
    HOLDER=models.ManyToManyField(User,related_name='%(class)screated')
    def __str__(self):
        return f"{self.sen} to {self.rec}";
    


    
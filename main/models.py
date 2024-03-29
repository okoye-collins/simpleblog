from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=225)
    tag = models.CharField(max_length=225, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()


    def __str__(self):
        return f'{self.title} | {self.author}'
    
    def get_absolute_url(self):
        return reverse('home')
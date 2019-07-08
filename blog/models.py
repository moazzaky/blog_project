from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    body = RichTextField(default='enter your text here')
    tags = TaggableManager()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_url',args=[str(self.id)])


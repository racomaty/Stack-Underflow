from django.db import models
from django.contrib.auth.models import User 
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='PostAuthor')
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='postsImages/', blank=True, null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='AnswerAuthor')
    text = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('-date',)
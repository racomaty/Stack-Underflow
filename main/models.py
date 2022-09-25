from django.db import models
from django.contrib.auth.models import User 
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='PostAuthor')
    title = models.CharField(max_length=200)
    description = RichTextUploadingField(blank=False, null=True)
    date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-date',)

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='AnswerAuthor')
    body = RichTextUploadingField(blank=False, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='PostAnswer', null=True)
    date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    votesUp = models.ManyToManyField(User, related_name='AnswerVotesUp', blank=True)
    votesDown = models.ManyToManyField(User, related_name='AnswerVotesDown', blank=True)
    
    def __str__(self):
        return self.post.title
    class Meta:
        ordering = ('-votes',)


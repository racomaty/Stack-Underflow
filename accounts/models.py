from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')

class Biography(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    biography = models.TextField(max_length=500, blank=True)
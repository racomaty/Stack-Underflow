from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', about, name='about'),
    path('post/<int:id>', post, name='post'),
    path('post/new/', newPost, name='newPost'),
    path('editPost/<int:id>', editPost, name='editPost'),
]
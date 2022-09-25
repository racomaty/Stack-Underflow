from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('post/<int:id>', post, name='post'),
    path('post/new/', newPost, name='newPost'),
    path('post/edit/<int:id>', editPost, name='editPost'),
    path('post/delete/<int:id>', deletePost, name='deletePost'),
    path('post/tag/<str:name>', TagIndexView, name='tagged'),
]
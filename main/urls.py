from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('post/search/', search, name='search'),
    path('post/<int:id>', post, name='post'),
    path('post/new/', newPost, name='newPost'),
    path('post/edit/<int:id>', editPost, name='editPost'),
    path('post/delete/<int:id>', deletePost, name='deletePost'),
    path('post/tag/<str:name>', TagSearch, name='tagged'),
    path('post/answer/new/<int:id>', newAnswer, name='newAnswer'),
    path('post/answer/edit/<int:id>', editAnswer, name='editAnswer'),
    path('post/answer/delete/<int:id>', deleteAnswer, name='deleteAnswer'),
    path('answer/<int:id>/up', answerUpVote, name='answerUpVote'),
    path('answer/<int:id>/down', answerDownVote, name='answerDownVote'),
]
from django.urls import path
from .views import *

app_name = 'chat'

urlpatterns = [
    path('', messages, name='messages'),
    path('newChat/', newChat, name='newChat'),
    path('chat/<str:username>/', chat, name='chat'),
    path('sendMessage/', sendMessage, name='sendMessage'),
]
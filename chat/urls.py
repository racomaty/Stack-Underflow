from django.urls import path
from .views import *

app_name = 'chat'

urlpatterns = [
    path('', messages, name='messages'),
    path('chat/new', newChat, name='newChat'),
    path('chat/<str:username>/', chat, name='chat'),
    path('chat/message/send', sendMessage, name='sendMessage'),
]
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Avatar
import os
from django.conf import settings
from .models import *


# Create your views here.
@login_required
def messages(request):
    return render(request, 'chat/messages.html', {'userAvatar': getAvatar(request.user), 'contacts': getContacts(request)})

def newChat(request):
    if request.method == 'POST':
        try:
            contact = User.objects.get(username=request.POST['contact'])
            contact.avatar = getAvatar(contact)
            return render(request, 'chat/chat.html', {'userAvatar': getAvatar(request.user), 'contact': contact, 'messages': getContactMessages(request, contact), 'contacts': getContacts(request)})
        except:
            return render(request, 'chat/messages.html', {'userAvatar': getAvatar(request.user), 'contacts': getContacts(request), 'error': 'User not found'})

def chat(request, username):
    try:
        contact = User.objects.get(username=username)
        contact.avatar = getAvatar(contact)
        return render(request, 'chat/chat.html', {'userAvatar': getAvatar(request.user), 'contact': contact, 'messages': getContactMessages(request, contact), 'contacts': getContacts(request)})
    except:
        return render(request, 'chat/chat.html', {'error': 'chat not found'})

def sendMessage(request):
    if request.method == 'POST':
        message = Message.objects.create(sender=request.user, receiver=User.objects.get(username=request.POST['username']), message=request.POST['message'])
        message.save()
        return redirect('chat:chat', username=request.POST['username'])
### Functions

def getContacts (request):
    if request.user.id:
        contacts = []
        for message in Message.objects.all().filter(sender=request.user):
            if message.receiver not in contacts:
                contacts.append(message.receiver)
        for message in Message.objects.all().filter(receiver=request.user):
            if message.sender not in contacts:
                contacts.append(message.sender)
        for contact in contacts:
            contact.avatar = getAvatar(contact)
        return contacts

def getContactMessages (request, contact):
    if request.user.id:
        messages = Message.objects.all().filter(sender=request.user, receiver=contact) | Message.objects.all().filter(sender=contact, receiver=request.user)
        for message in messages:
            message.sender.avatar = getAvatar(message.sender)
            if message.sender == request.user:
                message.sender.username = 'You'
        messages = reversed(messages)
        return messages

def getAvatar(user):
    if user.id:
        avList = Avatar.objects.all().filter(user=user.id)
        if len(avList) > 0:
            return avList[0].image.url
        else:
            return os.path.join(settings.MEDIA_URL, 'avatars/default.png')
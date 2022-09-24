from django.shortcuts import render
from accounts.models import Avatar
import os
from django.conf import settings

def inicio(request):
    if request.user.id:
        return render(request,"main/inicio.html", {'userAvatar': getAvatar(request)})
    return render(request,"main/inicio.html")

def about(request):
    return render(request,"main/about.html", {'userAvatar': getAvatar(request)})

def getAvatar (request):
    if request.user.id:
        avList = Avatar.objects.all().filter(user=request.user.id)
        if len(avList) > 0:
            return avList[0].image.url
        else:
            return os.path.join(settings.MEDIA_URL, 'avatars/default.png')
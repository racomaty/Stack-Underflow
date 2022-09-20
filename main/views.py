from django.shortcuts import render
from accounts.models import Avatar


def inicio(request):
    if request.user.id:
        avatarUrl = Avatar.objects.all().filter(user=request.user.id).first().image.url
        return render(request,"main/inicio.html", {'avatarUrl': f'accounts{avatarUrl}'})
    return render(request,"main/inicio.html")
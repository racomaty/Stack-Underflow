from django.shortcuts import render, redirect
from accounts.models import *
from .models import *
import os
from django.conf import settings
from .forms import *

def inicio(request):
    posts = Post.objects.all()
    if request.user.id:
        return render(request,"main/inicio.html", {'posts': posts, 'userAvatar': getAvatar(request)})
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

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request,"main/post.html", {'post': post, 'userAvatar': getAvatar(request)})

def newPost(request):
    postForm = PostForm(request.POST)
    if request.method == 'POST':

        if postForm.is_valid():
            user = request.user
            post = Post(title = postForm.cleaned_data['title'], 
                description = postForm.cleaned_data['description'], 
                tags = postForm.cleaned_data['tags'], 
                
                author = user
            )
            post.save()
            print(post.tags.all())
            return redirect('main:inicio')
        else:
            return render(request, 'main/post.html', {'form': postForm, 'userAvatar': getAvatar(request)})
    else:
        return render(request, 'main/newPost.html', {'form': postForm,'userAvatar': getAvatar(request)})

def editPost(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post.title = postForm.cleaned_data['title']
            post.description = postForm.cleaned_data['description']
            post.tags = postForm.cleaned_data['tags']
            post.image = postForm.cleaned_data['image']
            post.save()
            return redirect('main:post/<int:id>', id)
        else:
            return render(request, 'main/post.html', {'formErrors': postForm.errors, 'userAvatar': getAvatar(request)})
    else:
        return render(request, 'main/post.html', {'post': post, 'userAvatar': getAvatar(request)})
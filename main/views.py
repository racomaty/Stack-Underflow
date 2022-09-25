from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import *
from .models import *
from .forms import *
from taggit.models import Tag
from django.conf import settings
import os

def home(request):
    posts = Post.objects.all()
    for post in posts:
        post.author.avatar = getAvatar(post.author)
    return render(request,"main/home.html", {'posts': posts, 'userAvatar': getAvatar(request.user)})

def about(request):
    return render(request,"main/about.html", {'userAvatar': getAvatar(request.user)})

def TagIndexView(request, name):
    tag = Tag.objects.get(name=name)
    posts = Post.objects.filter(tags=tag)
    for post in posts:
        post.author.avatar = getAvatar(post.author)
    return render(request, 'main/home.html', {'posts': posts, 'tag': tag, 'userAvatar': getAvatar(request.user)})

def post(request, id):
    post = Post.objects.get(id=id)
    post.author.avatar = getAvatar(post.author)
    return render(request,"main/post.html", {'post': post, 'userAvatar': getAvatar(request.user)})

@login_required
def newPost(request):
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            form.save_m2m()
            return redirect('main:home')
        else:
            return render(request, 'main/newPost.html', { 'form': form, 'formErrors': form.errors, 'userAvatar': getAvatar(request.user)})
    else:
        return render(request, 'main/newPost.html', {'form': form, 'userAvatar': getAvatar(request.user)})

@login_required
def editPost(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            form.save_m2m()
            return redirect('main:home')
        else:
            return render(request, 'main/editPost.html', { 'form': form, 'formErrors': form.errors, 'userAvatar': getAvatar(request.user)})
    else:
        return render(request, 'main/editPost.html', {'form': form, 'post': post, 'userAvatar': getAvatar(request.user)})

@login_required
def deletePost(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        if request.user == post.author:
            post.delete()
        return redirect('main:home')
    else:
        return render(request, 'main/deletePost.html', {'post':post,'userAvatar': getAvatar(request.user)})

################ Funciones
def getAvatar(user):
    if user.id:
        avList = Avatar.objects.all().filter(user = user.id)
        if len(avList) > 0:
            return avList[0].image.url
        else:
            return os.path.join(settings.MEDIA_URL, 'avatars/default.jpeg')
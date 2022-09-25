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
    answers = Answer.objects.all().filter(post=post)
    alreadyAnswered = False
    for answer in answers:
        answer.author.avatar = getAvatar(answer.author)
        if answer.author == request.user:
            alreadyAnswered = True
    answerForm = AnswerForm()
    print(alreadyAnswered)
    return render(request,"main/newAnswer.html", {'post': post, 'answerForm': answerForm,'user': request.user, 'alreadyAnswered': alreadyAnswered, 'answers': answers,'userAvatar': getAvatar(request.user)})

@login_required
def newAnswer(request, id):
    form = AnswerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.post = Post.objects.get(id)
            obj.save()
            return redirect('main:post', id)
        else:
            return render(request, 'main/newPost.html', { 'form': form, 'formErrors': form.errors, 'userAvatar': getAvatar(request.user)})
    else:
        return render(request, 'main/newPost.html', {'form': form, 'userAvatar': getAvatar(request.user)})

@login_required
def answerUpVote(request, id):
    answer = Answer.objects.get(id=id)
    if request.user in answer.votesUp.all():
        return redirect('main:post', answer.post.id)
    if request.user in answer.votesDown.all():
        answer.votesDown.remove(request.user)
        answer.votes += 1
        answer.save()
        return redirect('main:post', answer.post.id)
    answer.votesUp.add(request.user)
    answer.votes += 1
    answer.save()
    return redirect('main:post', answer.post.id)

@login_required
def answerDownVote(request, id):
    answer = Answer.objects.get(id=id)
    if request.user in answer.votesDown.all():
        return redirect('main:post', answer.post.id)
    if request.user in answer.votesUp.all():
        answer.votesUp.remove(request.user)
        answer.votes -= 1
        answer.save()
        return redirect('main:post', answer.post.id)
    answer.votesDown.add(request.user)
    answer.votes -= 1
    answer.save()
    return redirect('main:post', answer.post.id)

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
            answers = Answer.objects.all().filter(post=post)
            for answer in answers:
                answer.delete()
        return redirect('main:home')
    else:
        return render(request, 'main/deletePost.html', {'post':post,'userAvatar': getAvatar(request.user)})

@login_required
def newAnswer(request, id):
    post = Post.objects.get(id=id)
    form = AnswerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.post = post
            obj.save()
            form.save_m2m()
            return redirect('main:post', id=post.id)
        else:
            return render(request, 'main/newAnswer.html', { 'form': form, 'formErrors': form.errors, 'userAvatar': getAvatar(request.user)})
    else:
        return render(request, 'main/newAnswer.html', {'form': form, 'post': post, 'userAvatar': getAvatar(request.user)})

@login_required
def editAnswer(request, id):
    answer = Answer.objects.get(id=id)
    post = answer.post
    form = AnswerForm(request.POST or None, instance=answer)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()
            return redirect('main:post', id=post.id)
        else:
            return render(request, 'main/editAnswer.html', { 'form': form, 'formErrors': form.errors,'answer': answer, 'userAvatar': getAvatar(request.user)})
    else:
        return render(request, 'main/editAnswer.html', {'form': form, 'post': post, 'answer': answer, 'userAvatar': getAvatar(request.user)})

@login_required
def deleteAnswer(request, id):
    answer = Answer.objects.get(id=id)
    post = answer.post
    if request.user == answer.author:
        answer.delete()
    return redirect('main:post', id=post.id)

################ Funciones
def getAvatar(user):
    if user.id:
        avList = Avatar.objects.all().filter(user = user.id)
        if len(avList) > 0:
            return avList[0].image.url
        else:
            return os.path.join(settings.MEDIA_URL, 'avatars/default.jpeg')
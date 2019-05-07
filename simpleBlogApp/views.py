from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

import datetime


def index(request):
    posts = Post.objects.all().order_by('-post_id')
    return render(request, 'index.html', context={'posts': posts})


def postNew(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.save()
            return redirect('index')
        else:
            return render(request, 'error.html')
    return redirect('index')


def postDetail(request, id):
    if Post.objects.filter(post_id = id).exists():
        post = Post.objects.get(post_id=id)
        return render(request, 'post.html', context={'post': post})
    return render(request, 'error.html')


def postDelete(request, id):
    if Post.objects.filter(post_id = id).exists():
        Post.objects.filter(post_id = id).delete()
        return redirect('index')
    return render(request, 'error.html')


def postEdit(request, id):
    if Post.objects.filter(post_id = id).exists():
        post = Post.objects.get(post_id=id)
        return render(request, 'post.html', context={'post': post})
    return render(request, 'error.html')
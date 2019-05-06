from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

import datetime


def index(request):
    posts = Post.objects.all().order_by('-post_id')
    return render(request, 'index.html', context={'posts': posts})


def postNew(request):
    posts = Post.objects.all().order_by('-post_id')

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            submission = form.save(commit=False)
            submission.save()
            return render(request, 'index.html', context={'posts': posts})
        else:
            return render(request, 'error.html')

    else:
        return render(request, 'index.html', context={'posts': posts})


def postDetail(request, id):
    if Post.objects.filter(post_id = id).exists():
        post = Post.objects.get(post_id=id)
        return render(request, 'post.html', context={'post': post})
    else:
        return render(request, 'error.html')


def postDelete(request, id):
    if Post.objects.filter(post_id = id).exists():
        post = Post.objects.get(post_id=id)
        return render(request, 'post.html', context={'post': post})
    else:
        return render(request, 'error.html')


def postEdit(request, id):
    if Post.objects.filter(post_id = id).exists():
        post = Post.objects.get(post_id=id)
        return render(request, 'post.html', context={'post': post})
    else:
        return render(request, 'error.html')
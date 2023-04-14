from django.shortcuts import render
from posts.models import Post


# Create your views here.

def index(request):
    posts = Post.objects.all() # renamed objects to items
    return render(request, 'posts/index.html',{'posts':posts})

def usingManager(request):
    posts = Post.objects.sorted()
    return render(request, 'posts/index.html',{'posts':posts})


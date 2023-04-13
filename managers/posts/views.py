from django.shortcuts import render
from posts.models import Post


# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html',{'posts':posts})

def usingManager(request):
    pass


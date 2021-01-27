from django.shortcuts import render

from .models import Post


def home_page(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})


def blog_page(request):
    return render(request, 'blog.html')
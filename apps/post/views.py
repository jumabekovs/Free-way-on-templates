from django.shortcuts import render

from .models import Post, ExtendPost
from ..category.models import CategoryPost


def home_page(request):
    posts = Post.objects.all()[:2]
    return render(request, 'index.html', locals())


def blog_page(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', locals())


def blog_detail(request, title):  # this function requires title to filter by a category
    post_category = Post.objects.filter(title=title)
    post_category_name = CategoryPost.objects.get(name=title)
    return render(request, 'blog_detail.html', locals())


def extend_post(request, pk):
    extends = ExtendPost.objects.filter(pk=pk)
    return render(request, "blog_detail.html", locals())


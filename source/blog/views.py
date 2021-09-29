from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blog(request):
    pro = Blog.objects.order_by('-date')
    context = {
        "projects": pro
    }
    return render(request, "blog_hello.html", context)


def detail(request, id):
    obj = get_object_or_404(Blog, pk=id)
    context = {
        "blog": obj
    }
    return render(request, 'blog_detail.html', context)

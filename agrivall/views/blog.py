
from django.shortcuts import render, redirect, get_object_or_404
from agrivall.models import PostBlog, TipoPost
from django.contrib.auth.decorators import login_required

def blog(request):

    posts = PostBlog.objects.all()

    return render(request, 'blog.html', {"posts": posts})

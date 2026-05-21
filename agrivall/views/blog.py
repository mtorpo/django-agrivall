
from django.shortcuts import render, redirect, get_object_or_404

def blog(request):
    return render(request, 'blog.html')
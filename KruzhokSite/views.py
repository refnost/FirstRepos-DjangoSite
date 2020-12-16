from django.shortcuts import render
from .models import Post
from django.utils import timezone

def profile(request):
    posts = Post.objects.all()
    return render(request, 'profile/index.html', {'posts': posts})

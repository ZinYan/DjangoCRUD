from django.shortcuts import render

# Create your views here.
from .models import Post

def posts_list(request, *args, **kwargs) :
  posts = Post.objects.all()
  context = {
    "posts" : posts
  }
  return render(request, "posts_list.html", context)
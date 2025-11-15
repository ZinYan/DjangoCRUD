from django.shortcuts import render, redirect

# Create your views here.
from .models import Post

def posts_list(request, *args, **kwargs) :
  posts = Post.objects.all()
  context = {
    "posts" : posts
  }
  return render(request, "posts_list.html", context)

def posts_read(request, pk):  
  post = Post.objects.get(id=pk)
  context = {
    "post" : post
  }
  return render(request, "posts_read.html", context)

def posts_create(request): 
  if request.method == "POST" :
    Post.objects.create(
    title=request.POST["title"],
    user=request.POST["user"],
    content=request.POST["content"],
    )
    return redirect("/posts")
  return render(request, "posts_create.html")

def posts_update(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.user = request.POST["user"]
        post.save()
        return redirect(f"/posts/{pk}")

    context = {"post": post}
    return render(request, "posts_update.html", context)
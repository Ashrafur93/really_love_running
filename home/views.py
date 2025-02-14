from django.shortcuts import render
from jogging_post.models import Post

# Create your views here.

class HomeList:
    template_name = "home/index.html"

def home(request):
    post = Post.objects.all()
    return render(
        request,
        "home/index.html", {"posts": post}
    )

class GalleryView:
    template_name = "home/gallery.html"

def gallery(request):
    post = Post.objects.all()
    return render(
        request,
        "home/gallery.html", {"posts": post}
    )
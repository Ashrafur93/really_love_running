from django.shortcuts import render
from django.http import HttpResponse
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
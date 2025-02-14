from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

class PostList:
    template_name = "jogging_post/jogging_post.html"

def jogging_post (request):
    return render(
        request,
        "jogging_post/jogging_post.html",
    )

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'jogging_post/jogging_post.html', {'post': post})
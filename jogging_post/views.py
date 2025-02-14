from django.shortcuts import render

class PostList:
    template_name = "jogging_post/jogging_post.html"

def jogging_post (request):
    return render(
        request,
        "jogging_post/jogging_post.html",
    )
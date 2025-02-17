from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required


class PostList:
    template_name = "jogging_post/jogging_post.html"


def jogging_post(request):
    return render(
        request,
        "jogging_post/jogging_post.html",
    )


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post).order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            body = request.POST.get('comment')
            Comment.objects.create(user=request.user, post=post, body=body)
            return redirect('post_detail', slug=slug)
        else:
            return redirect('login')  # Redirect to login if user is not authenticated

    return render(request, 'jogging_post/jogging_post.html', {'post': post, 'comments': comments})

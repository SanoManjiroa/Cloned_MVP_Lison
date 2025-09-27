from django.shortcuts import render
from .models import PostsPostPage

# def post(request):
#     posts = PostsPostPage.objects.all()
#     return render(request, "basedir_post_app.html", {"posts": posts})

def post(request):
    posts = PostsPostPage.objects.all()
    return render(request, "post_page.html", {"posts": posts})

def post_make(request):
    return render(request, "post_make.html")

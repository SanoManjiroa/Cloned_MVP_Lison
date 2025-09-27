from django.shortcuts import render,redirect
from .models import PostsPostPage
from .forms import PostsPostPageForm

# def post(request):
#     posts = PostsPostPage.objects.all()
#     return render(request, "basedir_post_app.html", {"posts": posts})

def post(request):
    posts = PostsPostPage.objects.all()
    return render(request, "post_page.html", {"posts": posts})
#
# def post_make(request):
#     return render(request, "post_make.html")

def post_make(request):
    if request.method == "POST":
        title = request.POST.get("post_title")
        content = request.POST.get("post_content")
        username = request.POST.get("username") or "Anonymous"
        color = request.POST.get("colorProfilePost") or "#FFFFFF"
        profile_img = request.FILES.get("Profile")  # ✅ handle uploaded file

        if title and content:
            PostsPostPage.objects.create(
                account_mode="writer",
                username=username,
                post_title=title,
                post_content=content,
                colorProfilePost=color,
                Profile=profile_img  # store uploaded image
            )
            return redirect("post")  # or success page
    return render(request, "post_make.html")

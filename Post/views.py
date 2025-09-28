from django.shortcuts import render, redirect
from .models import PostsPostPage
import requests
from django.conf import settings

def post(request):
    posts = PostsPostPage.objects.all()
    return render(request, "post_page.html", {"posts": posts})

def post_make(request):
    if request.method == "POST":
        title = request.POST.get("post_title")
        content = request.POST.get("post_content")
        username = request.POST.get("username") or "Anonymous"
        color = request.POST.get("colorProfilePost") or "#FFFFFF"
        profile_img = request.FILES.get("Profile")

        profile_url = None
        if profile_img and getattr(settings, "IMGBB_API_KEY", None):
            try:
                response = requests.post(
                    "https://api.imgbb.com/1/upload",
                    files={"image": profile_img},
                    data={"key": settings.IMGBB_API_KEY}
                )
                response.raise_for_status()
                profile_url = response.json()["data"]["url"]
            except Exception as e:
                print("ImgBB upload failed:", e)
                profile_url = None

        if title and content:
            PostsPostPage.objects.create(
                account_mode="writer",
                username=username,
                post_title=title,
                post_content=content,
                colorProfilePost=color,
                Profile_url=profile_url
            )
            return redirect("post")

    return render(request, "post_make.html")

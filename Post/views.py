import base64
import requests
from django.shortcuts import render, redirect
from .models import PostsPostPage
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
        profile_img = request.FILES.get("Profile")  # uploaded file

        profile_url = None
        if profile_img:
            # convert image to base64
            img_data = base64.b64encode(profile_img.read())
            response = requests.post(
                "https://api.imgbb.com/1/upload",
                data={
                    "key": settings.IMGBB_API_KEY,
                    "image": img_data
                }
            )
            if response.status_code == 200:
                profile_url = response.json()["data"]["url"]

        if title and content:
            PostsPostPage.objects.create(
                account_mode="writer",
                username=username,
                post_title=title,
                post_content=content,
                colorProfilePost=color,
                Profile_url=profile_url  # <-- store ImgBB URL
            )
            return redirect("post")

    return render(request, "post_make.html")

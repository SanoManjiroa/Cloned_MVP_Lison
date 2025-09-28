from django.db import models

class PostsPostPage(models.Model):
    ACCOUNT_CHOICES = [
        ('reader', 'Reader'),
        ('writer', 'Writer'),
        ('poet', 'Poet'),
    ]
    account_mode = models.CharField(max_length=30, choices=ACCOUNT_CHOICES)
    username = models.CharField(max_length=100)
    post_title = models.CharField(max_length=100, default="Untitled")
    post_content = models.TextField()
    colorProfilePost = models.CharField(max_length=7, default="#FFFFFF")
    Profile_url = models.URLField(blank=True, null=True)  # ✅ store ImgBB URL

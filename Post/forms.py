from django import forms
from .models import PostsPostPage

class PostsPostPageForm(forms.ModelForm):
    class Meta:
        model = PostsPostPage
        fields = ['account_mode', 'username', 'post_title', 'post_content', 'colorProfilePost', 'Profile']

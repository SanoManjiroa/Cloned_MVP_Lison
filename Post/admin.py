from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import PostsPostPage


# Admin formasi (rang tanlagich uchun)
class PostsPostPageForm(forms.ModelForm):
    class Meta:
        model = PostsPostPage
        fields = '__all__'
        widgets = {
            'colorProfilePost': forms.TextInput(attrs={'type': 'color'}),
        }


@admin.register(PostsPostPage)
class PostsPostPageAdmin(admin.ModelAdmin):
    form = PostsPostPageForm
    list_display = ("username", "account_mode", "profile_preview", "color_preview")

    def profile_preview(self, obj):
        if obj.Profile:
            return format_html('<img src="{}" width="50" height="50" />', obj.Profile.url)
        return "-"
    profile_preview.short_description = "Profile Image"

    def color_preview(self, obj):
        if obj.colorProfilePost:
            return format_html(
                '<div style="width: 30px; height: 30px; background-color:{}; border:1px solid #000"></div>',
                obj.colorProfilePost
            )
        return "-"
    color_preview.short_description = "Color"

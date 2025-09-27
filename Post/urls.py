from django.urls import path
from .views import post, post_make

urlpatterns = [
    path('', post, name='post'),
    path('postmake/', post_make,  name='post_make'),
]
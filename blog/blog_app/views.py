from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'



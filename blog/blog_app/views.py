from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    ordering = ['date_created']


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'



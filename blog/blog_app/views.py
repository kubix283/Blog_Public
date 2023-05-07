from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    ordering = ['date_created']


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'description']
    
    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse('post_detail', kwargs={"pk": pk})


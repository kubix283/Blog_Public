from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.views.generic import (ListView, DetailView,
                                  UpdateView, DeleteView,)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    ordering = ['date_created']


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            author = request.user
            post = form.save(commit=False)
            post.author = author
            post.save()
            messages.success(request, 'Post created successfully')
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'description']

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse('post_detail', kwargs={"pk": pk})


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

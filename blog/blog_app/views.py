from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic import (ListView, DetailView,
                                  UpdateView, DeleteView,)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    ordering = ['date_created']


# class PostDetailView(DetailView):
#     model = Post
#     context_object_name = 'post'
#     template_name = 'post_detail.html'

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


# @login_required(login_url="/login/")
def comment_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)      
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment posted successfully')
            return redirect('post_detail', post.pk)
        for error in list(form.errors.values()):
            messages.error(request, error)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'form': form, 'post': post, 'comments': comments})


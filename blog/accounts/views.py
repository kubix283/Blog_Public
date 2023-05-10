from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib import messages
from .forms import RegistrationUserForm
from blog_app.models import Post


def register(request):
    if request.user.is_authenticated:
        return redirect('/')   
    if request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Registration successful {user.username}')
            return redirect('/')   
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = RegistrationUserForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def logout_user(request):
    messages.info(request, f'Logout {request.user.username}')
    logout(request)
    return redirect('/')


def profile_user(request, username):
    user = request.user
    posts = Post.objects.filter(author__username=user.username).count()
    if user:
        return render(request, 'accounts/profile.html', {'user': user, 'posts': posts})


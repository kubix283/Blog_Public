from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationUserForm, UserUpdateForm
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

@login_required(login_url="/login/")
def profile_user(request, username):
    user = request.user
    posts = Post.objects.filter(author__username=user.username).count()
    return render(request, 'accounts/profile.html', {'user': user, 'posts': posts})


def edit_profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            user_form.create_thumbnail_100()
            messages.success(request, f'{user_form.username}, Your profile has been updated')
            return redirect('profile_user', user_form.username)
        
        for error in list(form.errors.values()):
            messages.error(request, error)
    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        return render(request, 'edit_profile.html', {'form': form})
    return redirect('post_list')
    

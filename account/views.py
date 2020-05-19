from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from  django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import User
from posted.models import Post

from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, LoginForm

def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + 'さん、はじめまして。ログインしてください。')
            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', {'form': form})


# def login_page(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('profile')
#         else:
#             messages.info(request, 'ユーザ名またはパスワードが違っています。')

#     context = {
#         'form': form
#         }
#     return render(request, 'accounts/login.html', context)

class LoginPage(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    mypost_objs = Post.objects.filter(author=request.user)
    qs = Post.objects.filter(author=request.user)
    paginator = Paginator(qs, 12) # Show 10 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'qs': qs,
        'page_obj': page_obj,
        'paginator': paginator,
        'myposts': mypost_objs,
        }
    return render(request, 'accounts/profile.html', context)


@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'accounts/profile_update.html', context)
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import Profile

def register_view(request):
    name = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phonenumber')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1 == password2:
        try:
            User.objects.create_user(username=name, email=email, password=password1)
            messages.success(request, 'Your account was created')
            user = authenticate(request, username=name, password=password1)
            Profile(user=user, phonenumber=phone).save()
            login(request, user)
        except:
            messages.warning(request, "your account couldn't be created")
    else:
        messages.warning(request, "The passwords don't match")
    return redirect('/')

def login_view(request):
    name = request.POST.get('username')
    password = request.POST.get('password1')
    login(request, authenticate(username=name, password=password))
    return redirect('/')


def logout_view(request):
    try:
        logout(request)
        messages.success(request, 'You have successfully logged out')
    except:
        messages.warning(request, "Something went wrong")
    return redirect('/')

def update_view(request):
    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    email = request.POST.get('email')
    phone = request.POST.get('number')
    user = request.user
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.save()
    profile = Profile.objects.get(user=user)
    profile.phonenumber = phone
    profile.save()
    messages.success(request, 'Your profile has been changed')
    return redirect('/')
    
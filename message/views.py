from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import Profile

def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {'user':request.user, 'profile':Profile.objects.get(user=request.user)})
    return render(request, "home.html", {})


def dashboard_view(request):
    if request.user.is_authenticated == False:
        messages.warning(request, 'Please login to continue')
    return redirect('/')

def bookclass_view(request):
    date = request.POST.get('date')
    profile = Profile.objects.get(user=request.user)
    profile.trail_class_timing = date
    profile.classbooked = True
    profile.save()
    messages.success(request, 'Your class is booked')
    return redirect('/')


def addcomment_view(request):
    comment = request.POST.get('comment')
    print(comment)
    profile = Profile.objects.get(user=request.user)
    profile.opinion = comment
    profile.save()
    messages.success(request, 'Your opinion has been saved')
    return redirect('/')
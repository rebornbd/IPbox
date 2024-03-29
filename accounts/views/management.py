from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms

from ..forms import SignUpForm


# login
def mylogin(request):
    invalidLogin = False

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('homepage'))
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
        
        invalidLogin = True
    
    return render(request, 'registration/login.html', context={'invalidLogin': invalidLogin})


# logout
def mylogout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
    return redirect("/")


# signup
def mysignup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('homepage'))

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


# user Types
def generalUser(user):
    res = False
    try:
        if user is None:
            raise ValueError('User Not Found!')
    
        if not user.is_active:
            raise ValueError('User Not Active!')
        
        if user.is_authenticated:
            res = True
    except Exception as err:
        pass
    return res

def adminUser(user):
    res = False
    try:
        if generalUser(user):
            if user.is_superuser or user.is_staff:
                res = True
    except Exception as err:
        pass
    return res

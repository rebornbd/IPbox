from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms


@login_required(login_url='accountsapp:login')
def userProfile(request):
    invalidUpdate = False

    if request.method == 'POST':
        firstname   = request.POST.get('firstname')
        lastname    = request.POST.get('lastname')
        email       = request.POST.get('email')

        try:
            f = forms.EmailField()
            
            if not email == "":
                myEmail = f.clean(email)

            userId = request.user.id
            user = User.objects.get(pk=userId)

            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.save()

            return HttpResponseRedirect(reverse('homepage'))
        except Exception as err:
            invalidUpdate = True
    
    context = {
        'firstname': request.user.first_name,
        'lastname': request.user.last_name,
        'email': request.user.email,
        'invalidUpdate': invalidUpdate
    }
    return render(request, 'accounts/profile.html', context=context)

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from IPbox.settings import MEDIA_ROOT
from django.urls import reverse
from django import forms
import uuid
import os

from ..models import UserProfile


@login_required(login_url='accountsapp:login')
def userProfile(request):
    invalidUpdate = False

    if request.method == 'POST':
        firstname   = request.POST.get('firstname')
        lastname    = request.POST.get('lastname')
        email       = request.POST.get('email')
        photo       = request.FILES.get('photo')

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

            # uploadProfilePic(photo, user)
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


def uploadProfilePic(photo, user):
    photoValidExtensions = ['.jpg', '.jpeg', '.gif', '.png', '.bmp']
    photoMaxSize = 5242880

    if photo is not None:
        photoExtension = os.path.splitext(photo.name)[1]
        photoSize = photo.size

        if photoExtension in photoValidExtensions and photoSize <= photoMaxSize:
            uniqueName = uniqueFileName() + photoExtension
            fs = FileSystemStorage(location=str(MEDIA_ROOT)+'/profiles/')
            filename = fs.save(uniqueName, photo)
            uploaded_file_url = fs.url(filename)

            filterUser = UserProfile.objects.filter(user=user)
            # update profile image
            if len(filterUser) > 0:
                mainUser = filterUser[0]
                up = mainUser.userprofile

                up.photo = uploaded_file_url
                up.save()
                pass
            else:
                up = UserProfile(user=user, photo=uploaded_file_url)
                up.save()
                pass

            return True
    return False


def uniqueFileName():
    filename = str(uuid.uuid4())
    return filename

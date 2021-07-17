from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'enter username'}),
        max_length=50, required=True,
        label='',
        help_text='',
        # label='Username ',
        # help_text='enter a valid username!'
    )
    email = forms.CharField(
        widget = forms.EmailInput(attrs={'placeholder': 'enter email'}),
        max_length=200, required=False,
        label='',
        help_text='',
        # label='Email ',
        # help_text='enter a valid email!'
    )
    password1 = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder': 'enter password'}),
        label = '',
        help_text = ''
        # label = 'Password ',
        # help_text = 'enter a valid password!'
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder': 'enter confirm password'}),
        label = '',
        help_text = ''
        # label = 'Confirm password ',
        # help_text = 'enter the same password as before!'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


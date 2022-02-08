from django import forms
from  django.contrib.auth.forms import  UserCreationForm
from  django.contrib.auth.models import User

# model for defining login form in database
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile

from accounts.models import Contact


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields='__all__'


class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude=['user','username','email']
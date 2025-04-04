from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=8, widget=forms.PasswordInput)


class SignupForm(ModelForm):
    
    class Meta:
        model = CustomUser
        fields = '__all__'

from django.core import validators
from django import forms
from .models import user

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=user
        fields=['name','email','password']
        widgets={
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.EmailInput(attrs={'class':'form-control'}),
            'Password': forms.PasswordInput(attrs={'class':'form-control'}),
        }
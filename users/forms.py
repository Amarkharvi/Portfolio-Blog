from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password1',
            'password2'
        ]

class UpdateUser(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model =User
        fields=['username','first_name','last_name','email']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['image']         
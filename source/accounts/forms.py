from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

from .models import AppUser


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone', 'avatar')


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'phone', 'avatar']

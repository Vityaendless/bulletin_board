from django.contrib.auth.forms import UserCreationForm

from .models import AppUser


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone', 'avatar')

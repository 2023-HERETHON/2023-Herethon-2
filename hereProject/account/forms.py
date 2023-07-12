from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields = ['username', 'email', 'password1','password2','nickname']
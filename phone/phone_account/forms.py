from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

phone_Account = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password2')
        
class SignupForm(UserCreationForm):
    class Meta:
        model = phone_Account
        fields = ['username','gender','age','email','shelter']


class LoginForm(AuthenticationForm):
    pass
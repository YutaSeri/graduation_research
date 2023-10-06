from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account
from django.contrib.auth import get_user_model

Account = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password2')
        
class SignupForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username','gender','age','email','shelter']


class LoginForm(AuthenticationForm):
    pass
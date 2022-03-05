from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




#signup form
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=300)


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
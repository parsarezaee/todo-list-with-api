from tempfile import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView, LogoutView




#signup view
class SignupUser(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('todo:home')
    template_name = 'account/signupuser.html'
    


#login view 
class LoginUser(LoginView):
    template_name = 'account/loginuser.html'

#logout view 
class LogoutUser(LogoutView):
    template_name = 'todo/home.html'
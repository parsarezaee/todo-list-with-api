from tempfile import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegisterForm


#signup view
class SignupUser(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('todo:home')
    template_name = 'account/signupuser.html'

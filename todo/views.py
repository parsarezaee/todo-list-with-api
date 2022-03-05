from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import UserRegisterModel



def home(request):
    return render(request, 'todo/home.html')


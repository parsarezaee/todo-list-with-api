from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout



#signup view
class SignupUser(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('account:loginuser')
    template_name = 'account/signupuser.html'
    


#login view 
class LoginUser(LoginView):
    template_name = 'account/loginuser.html'

#logout view 
class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('todo:home')

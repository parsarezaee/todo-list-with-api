from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from .forms import UserRegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login








#signup view
class SignupUser(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    success_message = "User created successfully"
    template_name = 'registration/signupuser.html'

    def forn_valid(self, form):
        super(SignupUser, self).form_valid(form)
        #the form is valid, automatically sign-in the user
        user = authenticate(self.request,
        username = form.cleaned_data['username'],
        password = form.cleaned_data['password']   
    )
        if user == None:
            return self.render_to_response(self.get_context_data(form=form))

        else:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())

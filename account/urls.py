from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.SignupUser.as_view(), name='signupuser')
]

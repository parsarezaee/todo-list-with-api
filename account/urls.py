from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('signup/', views.SignupUser.as_view(), name='signupuser'),
    path('login/', views.LoginUser.as_view(), name='loginuser'),
]

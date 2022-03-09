from django.urls import path, re_path, include
from . import views




app_name = 'account'
urlpatterns = [
    path('signup/', views.SignupUser.as_view(), name='signupuser'),

]

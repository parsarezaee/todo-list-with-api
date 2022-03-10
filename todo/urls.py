from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.createtodo, name='createtodo'),
    path('cuurent/', views.currenttodos, name='currenttodos'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo')

]

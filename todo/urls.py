from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.createtodo, name='createtodo'),
    path('cuurent/', views.currenttodos, name='currenttodos'),

    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/completed', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo')
]

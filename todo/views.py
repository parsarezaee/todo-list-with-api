from distutils.log import log
from webbrowser import get
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from .models import TodoModel




def home(request):
    return render(request, 'todo/home.html')


#create todo
@login_required
def createtodo(request):
    if request.method == "GET":
        form = TodoForm
        return render(request, 'todo/createtodo.html', {'form':form})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('todo:home')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form':form, 'error':'Bad data passed in. Try again'})



#current user's todos
@login_required
def currenttodos(request):
    todos =TodoModel.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'todo/currenttodos.html', {'todos':todos})  




#show completed todos
@login_required
def completedtodos(request):
    todos = TodoModel.objects.filter(user=request.user, datecompleted__isnull = False).order_by('-datecompleted')
    return render(request, 'todo/completedtodos.html', {'todos':todos})






@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(TodoModel, pk=todo_pk, user=request.user )
    if request.method == "GET":
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('todo:currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form, 'error':'Bad info'})

        



#show completed todos for user
@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(TodoModel, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('todo:currenttodos')



#delete todo
@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(TodoModel, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:currenttodos')
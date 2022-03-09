from django.shortcuts import render, redirect
from .forms import TodoForm





def home(request):
    return render(request, 'todo/home.html')


#create todo
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
from django.shortcuts import render,redirect
from .forms import TodoForm
from .models import Todo

def todo(request):
    message = None
    tasks = None
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            completed = form.cleaned_data['completed']
            Todo.objects.create(title=title, completed=completed)
            message = 'Added sucssesfully'
    tasks = Todo.objects.all()
    return render(request, 'todo.html',{'form':form, 'message':message, 'tasks':tasks})

def todo_delete(request, id):
    task = Todo.objects.get(id=id)
    task.delete()
    print(id)
    print(Todo.objects.all())
    return redirect('todo')
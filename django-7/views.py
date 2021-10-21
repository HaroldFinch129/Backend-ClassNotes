from django.shortcuts import redirect, render
from todo.models import Todo
def home(request):
    return render(request, "todo/home.html")
def todo_list(req):
    todos = Todo.objects.all()
    context = {
        'todos':todos
    }
    return redirect(req,'todo/todo_list.html', context)
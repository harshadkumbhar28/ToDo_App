from django.shortcuts import render, redirect
from .models import todo


# Create your views here.

def ToDoApp(request):
    Todo = todo.objects.all()
    context = {
        "Todo": Todo
    }

    return render(request, 'index.html', context)


def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        date = request.POST.get("date")
        status = request.POST.get("status")

        toDo = todo(
            Title=title,
            Description=description,
            Date=date,
            Status=status
        )

        toDo.save()
        return redirect('index')
    return render(request, 'index.html')


def edit(request):
    Todo = todo.objects.all()
    context = {
        "Todo": Todo
    }
    return render(request, 'index.html', context)


def update(request, id):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        date = request.POST.get("date")
        status = request.POST.get("status")

        toDo = todo(
            id=id,
            Title=title,
            Description=description,
            Date=date,
            Status=status
        )
        toDo.save()
        return redirect('index')
    return render(request, 'index.html')


def delete(request, id):
    Todo = todo.objects.filter(id=id)
    Todo.delete()
    context = {
        "Todo": Todo
    }
    return redirect('index')

    return render(request, 'index.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User, Category, Task
from .forms import AddTaskForm, TaskFilterForm


def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks':tasks})

def tasks(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'task.html', {'task':task})

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = AddTaskForm(request.POST or None, instance=task)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated")
            return redirect('home')
    return render(request, 'update_task.html', {'form':form})

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    messages.success(request, "Task Deleted")
    return redirect('home')

def add_task(request):
    form = AddTaskForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_task = form.save()
            messages.success(request, "Task Added")
            return redirect('home')
    return render(request, 'add_task.html', {'form':form})



def view_report(request):
    form = TaskFilterForm(request.GET or None)
    tasksOrig = Task.objects.all()
    tasks = tasksOrig
    statistic = tasks.raw("Select id, COUNT(DISTINCT user_id) as cnt FROM playground_task")
    users = 0
    for item in statistic:
        users = item.cnt
    statistic = tasks.raw("Select id, COUNT(*) as cnt FROM playground_task")
    queries = 0
    for item in statistic:
        queries = item.cnt
    if request.method == "GET":
        if form.is_valid():
            start_due_date = form.cleaned_data.get('start_due_date')
            end_due_date = form.cleaned_data.get('end_due_date')
            if start_due_date and end_due_date:
                tasks = tasksOrig.raw("SELECT * FROM playground_task WHERE due_date >= %s AND due_date <= %s", [start_due_date, end_due_date])
                statistic = tasksOrig.raw("Select id, Count(*) as cnt FROM (SELECT * FROM playground_task WHERE due_date >= %s AND due_date <= %s)", [start_due_date, end_due_date])
                for item in statistic:
                    queries = item.cnt
                statistic = tasksOrig.raw("Select id, Count(DISTINCT user_id) as cnt FROM (SELECT * FROM playground_task WHERE due_date >= %s AND due_date <= %s)", [start_due_date, end_due_date])
                for item in statistic:
                    users = item.cnt
    return render(request, 'view_report.html', {'form':form, 'tasks':tasks, 'users':users, 'queries': queries})

# Create your views here.

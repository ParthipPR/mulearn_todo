from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.contrib.auth.models import User, auth
from datetime import date

# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def updatepage(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "update.html",{'task':task})

def tasks(request):
    today = date.today()
    pending_tasks = Task.objects.filter(completed=False, deadline__gte=today)
    completed_tasks = Task.objects.filter(completed=True)
    expired_tasks = Task.objects.filter(completed=False, deadline__lt=today)

    tasks_count = pending_tasks.count() + completed_tasks.count() + expired_tasks.count()

    return render(request, "tasks.html", {
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
        'expired_tasks': expired_tasks,
        'tasks':tasks_count
    })

def completed(request, task_id):
    task_instance = get_object_or_404(Task, pk=task_id)
    task_instance.completed = True
    task_instance.save()
    return redirect("tasks")

def delete(request, task_id):
    task_instance = get_object_or_404(Task, pk=task_id)
    task_instance.delete()
    return redirect("tasks")


def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_date = request.POST.get('task_date')

        user = get_object_or_404(User,pk=1)
        task = Task.objects.create(
            contents=task_name,
            deadline=task_date,
            user=user
        )
        
        return redirect('tasks')  
    return redirect('tasks')  

def update(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id)

        task.contents = request.POST.get('task_name')
        task.deadline = request.POST.get('task_date')
        task.save()

        return redirect('tasks')
    return redirect('tasks')
    

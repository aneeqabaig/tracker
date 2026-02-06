from django.shortcuts import render, redirect, get_object_or_404
from .models import RoutineTask
from datetime import date


def dashboard(request):
    today = date.today()
    tasks = RoutineTask.objects.filter(scheduled_date=today).order_by("start_time")
    return render(request, "routines/dashboard.html", {"tasks": tasks})


def toggle_task(request, task_id):
    task = get_object_or_404(RoutineTask, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("dashboard")

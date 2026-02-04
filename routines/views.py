from django.shortcuts import render
from .models import RoutineTask
from datetime import date


def dashboard(request):
    today = date.today()
    tasks = RoutineTask.objects.filter(scheduled_date=today).order_by("start_time")
    return render(request, "routines/dashboard.html", {"tasks": tasks})

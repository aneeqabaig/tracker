from django.shortcuts import render, redirect, get_object_or_404
from .models import RoutineTask
from datetime import datetime, date, timedelta
from django.utils.timezone import localtime, make_naive

# --- Dashboard View ---
def dashboard_view(request):
    now = make_naive(localtime())  # convert aware datetime to naive
    today = date.today()
    tasks_today = RoutineTask.objects.filter(scheduled_date=today)

    current_task = None
    next_task = None
    pending_tasks = []

    for t in tasks_today:  # <-- use tasks_today, not undefined 'tasks'
        task_start = datetime.combine(t.scheduled_date, t.start_time)  # naive datetime
        task_end = task_start + timedelta(minutes=t.duration_minutes)
        
        if task_start <= now <= task_end and not t.is_completed:
            current_task = t

        elif task_start > now and not t.is_completed:
            if not next_task or task_start < datetime.combine(next_task.scheduled_date, next_task.start_time):
                next_task = t

        elif task_end < now and not t.is_completed:
            pending_tasks.append(t)

    # Progress calculation
    progress = {}
    for track in ['career', 'education', 'health']:
        track_tasks = RoutineTask.objects.filter(track=track)
        completed = track_tasks.filter(is_completed=True).count()
        total = track_tasks.count()
        progress[track] = int((completed / total) * 100) if total else 0

    return render(request, 'routines/dashboard.html', {
        'current_task': current_task,
        'next_task': next_task,
        'pending_tasks': pending_tasks,
        'progress': progress
    })


# --- Toggle Task Completion ---
def toggle_task(request, task_id):
    task = get_object_or_404(RoutineTask, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('dashboard')

# --- Add Task ---
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        track = request.POST.get('track')
        scheduled_date = request.POST.get('scheduled_date')
        start_time = request.POST.get('start_time')
        duration = request.POST.get('duration')
        RoutineTask.objects.create(
            title=title,
            track=track,
            scheduled_date=scheduled_date,
            start_time=start_time,
            duration_minutes=duration
        )
        return redirect('dashboard')
    return render(request, 'routines/add_task.html')

# --- Track Detail View ---
def track_detail(request, track):
    tasks = RoutineTask.objects.filter(track=track).order_by('scheduled_date', 'start_time')
    return render(request, 'routines/track_detail.html', {
        'track': track.capitalize(),
        'tasks': tasks
    })
def edit_task(request, task_id):
    task = get_object_or_404(RoutineTask, id=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.track = request.POST.get('track')
        task.scheduled_date = request.POST.get('scheduled_date')
        task.start_time = request.POST.get('start_time')
        task.duration_minutes = request.POST.get('duration')
        task.save()
        return redirect('track_detail', track=task.track)

    return render(request, 'routines/edit_task.html', {'task': task})

import os
import django
from datetime import date, time, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from routines.models import RoutineTask

# --- Career Track Tasks ---
career_tasks = [
    {"title": "Python Core: Lists, Tuples, Dicts", "duration": 60},
    {"title": "Python Core: Comprehensions & Generators", "duration": 45},
    {"title": "Python OOP: Classes & Inheritance", "duration": 60},
    {"title": "Advanced Python: Async & Threading", "duration": 60},
    {"title": "DSA: Arrays + Strings", "duration": 60},
    {"title": "DSA: Linked Lists + Stacks", "duration": 60},
    {"title": "OOD: SOLID & Design Patterns", "duration": 60},
]

# --- Education Track Tasks ---
education_tasks = [
    {"title": "IELTS Practice Reading", "duration": 30},
    {"title": "IELTS Practice Writing", "duration": 30},
    {"title": "Masters Research: University List", "duration": 45},
    {"title": "Masters Prep: SOP Draft", "duration": 60},
]

# --- Health & Mindset Tasks ---
health_tasks = [
    {"title": "Morning Walk / Stretch", "duration": 20},
    {"title": "Workout / Strength Training", "duration": 45},
    {"title": "Meditation / Mindset", "duration": 15},
    {"title": "Sleep Discipline Check", "duration": 10},
]

# --- Assign dates/times ---
start_date = date.today()
tasks_to_add = []

for i, t in enumerate(career_tasks):
    tasks_to_add.append(RoutineTask(
        title=t['title'],
        track='career',
        scheduled_date=start_date + timedelta(days=i),
        start_time=time(hour=7, minute=0),
        duration_minutes=t['duration']
    ))

for i, t in enumerate(education_tasks):
    tasks_to_add.append(RoutineTask(
        title=t['title'],
        track='education',
        scheduled_date=start_date + timedelta(days=i),
        start_time=time(hour=18, minute=0),
        duration_minutes=t['duration']
    ))

for i, t in enumerate(health_tasks):
    tasks_to_add.append(RoutineTask(
        title=t['title'],
        track='health',
        scheduled_date=start_date + timedelta(days=i),
        start_time=time(hour=6, minute=0),
        duration_minutes=t['duration']
    ))

# --- Save to database ---
RoutineTask.objects.bulk_create(tasks_to_add)
print(f"✅ Added {len(tasks_to_add)} tasks!")
from routines.models import RoutineTask
from datetime import date, time, timedelta

# --- Career Track Tasks ---
career_tasks = [
    {"title": "Python Core: Lists, Tuples, Dicts", "duration": 60},
    {"title": "Python Core: Comprehensions & Generators", "duration": 45},
    {"title": "Python OOP: Classes & Inheritance", "duration": 60},
    {"title": "Advanced Python: Async & Threading", "duration": 60},
    {"title": "DSA: Arrays + Strings", "duration": 60},
    {"title": "DSA: Linked Lists + Stacks", "duration": 60},
    {"title": "OOD: SOLID & Design Patterns", "duration": 60},
]

# --- Education Track Tasks ---
education_tasks = [
    {"title": "IELTS Practice Reading", "duration": 30},
    {"title": "IELTS Practice Writing", "duration": 30},
    {"title": "Masters Research: University List", "duration": 45},
    {"title": "Masters Prep: SOP Draft", "duration": 60},
]

# --- Health & Mindset Tasks ---
health_tasks = [
    {"title": "Morning Walk / Stretch", "duration": 20},
    {"title": "Workout / Strength Training", "duration": 45},
    {"title": "Meditation / Mindset", "duration": 15},
    {"title": "Sleep Discipline Check", "duration": 10},
]

start_date = date.today()
tasks_to_add = []

for i, t in enumerate(career_tasks):
    tasks_to_add.append(RoutineTask(
        title=t['title'],
        track='career',
        scheduled_date=start_date + timedelta(days=i),
        start_time=time(hour=7, minute=0),
        duration_minutes=t['duration']
    ))

for i, t in enumerate(education_tasks):
    tasks_to_add.append(RoutineTask(
        title=t['title'],
        track='education',
        scheduled_date=start_date + timedelta(days=i),
        start_time=time(hour=18, minute=0),
        duration_minutes=t['duration']
    ))

for i, t in enumerate(health_tasks):
    tasks_to_add.append(RoutineTask(
        title=t['title'],
        track='health',
        scheduled_date=start_date + timedelta(days=i),
        start_time=time(hour=6, minute=0),
        duration_minutes=t['duration']
    ))

RoutineTask.objects.bulk_create(tasks_to_add)
print(f"✅ Added {len(tasks_to_add)} tasks!")

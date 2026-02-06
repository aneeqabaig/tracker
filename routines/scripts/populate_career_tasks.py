from datetime import date, timedelta, time
from routines.models import RoutineTask

# --- Configuration ---
start_date = date.today()
num_days = 90  # 3 months

# Daily blocks
morning_block = [
    {"title": "DSA Practice", "duration": 30},
    {"title": "Python OOP", "duration": 30}
]

evening_block = [
    {"title": "LeetCode Problem", "duration": 30},
    {"title": "OOD Study", "duration": 30},
    {"title": "Project / Refactor", "duration": 30}
]

# Start times
morning_start = time(5, 30)  # 5:30 AM
evening_start = time(18, 0)  # 6:00 PM

def add_minutes(t, minutes):
    from datetime import datetime, timedelta
    dt = datetime.combine(date.today(), t)
    dt += timedelta(minutes=minutes)
    return dt.time()

# --- Populate tasks ---
for day_offset in range(num_days):
    task_date = start_date + timedelta(days=day_offset)

    # Morning block
    current_time = morning_start
    for block in morning_block:
        RoutineTask.objects.create(
            title=block["title"],
            track="career",
            scheduled_date=task_date,
            start_time=current_time,
            duration_minutes=block["duration"]
        )
        current_time = add_minutes(current_time, block["duration"])

    # Evening block
    current_time = evening_start
    for block in evening_block:
        RoutineTask.objects.create(
            title=block["title"],
            track="career",
            scheduled_date=task_date,
            start_time=current_time,
            duration_minutes=block["duration"]
        )
        current_time = add_minutes(current_time, block["duration"])

print(f"{num_days * (len(morning_block)+len(evening_block))} Career Track tasks created!")

# routines/models.py
from django.db import models

TRACK_CHOICES = [
    ('career', 'Career'),
    ('education', 'Education'),
    ('health', 'Health & Mindset'),
]

class RoutineTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    # track = models.CharField(max_length=20, choices=TRACK_CHOICES, default='career')  # ✅ track field
    scheduled_date = models.DateField()
    start_time = models.TimeField()
    duration_minutes = models.IntegerField(default=30)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    track = models.CharField(
    max_length=20,
    choices=[('career', 'Career'), ('education', 'Education'), ('health', 'Health & Mindset')],
    default='career'
)


    def __str__(self):
        return self.title

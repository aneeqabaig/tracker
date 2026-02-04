from django.contrib import admin
from .models import RoutineTask


@admin.register(RoutineTask)
class RoutineTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "scheduled_date", "start_time", "duration_minutes", "is_completed")
    list_filter = ("scheduled_date", "is_completed")
    search_fields = ("title",)

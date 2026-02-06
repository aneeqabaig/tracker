from django.urls import path
from . import dashboard

urlpatterns = [
    path('', dashboard.dashboard_view, name='dashboard'),
    path('toggle/<int:task_id>/', dashboard.toggle_task, name='toggle_task'),
    path('add/', dashboard.add_task, name='add_task'),

    path('track/<str:track>/', dashboard.track_detail, name='track_detail'),
    path('task/<int:task_id>/edit/', dashboard.edit_task, name='edit_task'),
]

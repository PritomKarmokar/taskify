from django.urls import path

from tasks.views import (
    TaskListAPIView,
    TaskCreateAPIView,
)
urlpatterns = [
    path('tasks/', TaskListAPIView.as_view(), name='tasks-all'),
    path('tasks/create/', TaskCreateAPIView.as_view(), name='tasks-create'),
]
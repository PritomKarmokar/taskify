from django.urls import path

from tasks.views import (
    TaskListAPIView,
    TaskCreateAPIView,
    TaskUpdateAPIView,
    TaskDeleteAPIView,
    TaskRetrieveAPIView
)

urlpatterns = [
    path(
        '',
        TaskListAPIView.as_view(),
        name='tasks-all'
    ),
    path(
        'create/',
        TaskCreateAPIView.as_view(),
        name='tasks-create'
    ),
    path(
        'update/<int:task_id>/',
        TaskUpdateAPIView.as_view(),
        name='tasks-update'
    ),
    path(
        'delete/<int:task_id>/',
        TaskDeleteAPIView.as_view(),
        name='tasks-delete'
    ),
    path(
        'retrieve/<int:task_id>/',
        TaskRetrieveAPIView.as_view(),
        name='tasks-retrieve'
    )
]
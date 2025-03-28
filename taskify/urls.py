from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tasks/admin/', admin.site.urls),
    path('api/tasks/', include('tasks.urls')),
]

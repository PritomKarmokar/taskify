from django.contrib import admin
from tasks.models.task import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'status'
    )
    ordering = ('created_at',)
    search_fields = (
        'title',
        'description',
        'status',
        'created_at',
        'due_date',
    )
from datetime import timedelta

from django.db import models
from django.utils import timezone

from tasks.models.choice_fields import Status

def default_due_date():
    return timezone.now() + timedelta(days=1)

class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.INITIATED
    )
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(
        default=default_due_date,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title + " --> " + self.status

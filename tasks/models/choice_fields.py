from django.db import models

class Status(models.TextChoices):
    INITIATED = 'initiated', "Initiated"
    IN_PROGRESS = 'in_progress', "In Progress"
    COMPLETED = 'completed', "Completed"
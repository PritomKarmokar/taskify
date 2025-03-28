from django.utils import timezone

from rest_framework import serializers

from tasks.models.task import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status','created_at', 'due_date')

    def validate(self, attrs):
        due_date = attrs.get('due_date')
        current_time = timezone.now()
        created_at = attrs.get('created_at', current_time)

        if due_date and due_date < current_time:
            raise serializers.ValidationError({"due_date": "Due date cannot be in the past."})

        if due_date and due_date < created_at:
            raise serializers.ValidationError({"due_date": "Due date must be after created_at."})

        return attrs
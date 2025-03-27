from datetime import timedelta

from django.urls import reverse
from django.utils import timezone

from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from tasks.models.task import Task
from tasks.serializers import TaskSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_task(title="", description="", task_status="", due_date=None):
        if title != "" and description != "" and task_status != "":

            if not due_date:
                due_date = timezone.now() + timedelta(days=1)

            Task.objects.create(
                title=title,
                description=description,
                status=task_status,
                due_date=due_date
            )

    def setUp(self):
        self.create_task(title="Test Task 01", description="Task Description", task_status="initiated")
        self.create_task(title="Test Task 02", description="Task Description", task_status="in_progress")


class GetAllTasksTest(BaseViewTest):
    def test_get_all_tasks(self):
        response = self.client.get(reverse('tasks-all'))
        expected = Task.objects.all()
        serializer = TaskSerializer(expected, many=True)

        expected_response = {
            "message": "Available tasks",
            "tasks": serializer.data,
        }

        self.assertEqual(response.data, expected_response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
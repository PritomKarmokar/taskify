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

            task = Task.objects.create(
                title=title,
                description=description,
                status=task_status,
                due_date=due_date
            )

            return task


    def setUp(self):
        task_1 = self.create_task(title="Test Task 01", description="Task Description", task_status="initiated")
        task_2 = self.create_task(title="Test Task 02", description="Task Description", task_status="in_progress")
        self.task_id = task_1.id # using for update, retrieve and delete test operation

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

class CreateTaskTest(BaseViewTest):
    def test_create_task(self):
        task_data = {
            "title": "New Task",
            "description": "Do the coding assignment",
            "status": "initiated",
        }
        response = self.client.post(
            reverse('tasks-create'),
            task_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UpdateTaskTest(BaseViewTest):
    def test_update_task(self):
        task_data = {
            "title": "Updated Task",
        }
        response = self.client.patch(
            reverse('tasks-update', kwargs={'task_id': self.task_id}),
            task_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class RetrieveTaskTest(BaseViewTest):
    def test_retrieve_task(self):
        response = self.client.get(
            reverse('tasks-retrieve', kwargs={'task_id': self.task_id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class DeleteTaskTest(BaseViewTest):
    def test_delete_task(self):
        response = self.client.delete(
            reverse('tasks-delete', kwargs={'task_id': self.task_id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
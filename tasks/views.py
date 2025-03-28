from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from tasks.models import Task
from tasks.serializers import TaskSerializer

class TaskListAPIView(APIView):
    serializer_class = TaskSerializer

    def get(self, request: Request) -> Response:
        tasks = Task.objects.all()
        if len(tasks) <= 0:
            response = {
                "message": "Currently, there are no tasks yet.",
            }
        else:
            serializer = self.serializer_class(tasks, many=True)
            response = {
                "message": "Available tasks",
                "tasks": serializer.data,
            }

        return Response(data=response, status=status.HTTP_200_OK)

class TaskCreateAPIView(APIView):
    serializer_class = TaskSerializer

    @swagger_auto_schema(request_body=TaskSerializer)
    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "New Task created",
                "task": serializer.data,
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskRetrieveAPIView(APIView):
    serializer_class = TaskSerializer

    def get(self, request: Request, task_id: int) -> Response:
        task = get_object_or_404(Task, id=task_id)
        serializer = self.serializer_class(instance=task)
        response = {
            "message": "Retrieved task",
            "data": serializer.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)

class TaskUpdateAPIView(APIView):
    serializer_class = TaskSerializer

    def patch(self, request: Request, task_id: int) -> Response:
        data = request.data
        task = get_object_or_404(Task, id=task_id)

        serializer = self.serializer_class(instance=task, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Task updated successfully",
                "data": serializer.data,
            }
            return Response(data=response, status=status.HTTP_200_OK)

class TaskDeleteAPIView(APIView):
    def delete(self, request: Request, task_id: int) -> Response:
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        response = {
            "message": f"Task with Id {task_id} deleted successfully",
        }
        return Response(data=response, status=status.HTTP_204_NO_CONTENT)
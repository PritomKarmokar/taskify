from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import Task
from tasks.serializers import TaskSerializer

class TaskListAPIView(APIView):
    serializer_class = TaskSerializer

    def get(self, request: Request) -> Response:
        tasks = Task.objects.all()
        serializer = self.serializer_class(tasks, many=True)
        response = {
            "message": "Available tasks",
            "tasks": serializer.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)

class TaskCreateAPIView(APIView):
    serializer_class = TaskSerializer
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
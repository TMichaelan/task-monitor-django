import csv
import os
from rest_framework import viewsets
from rest_framework.response import Response
from django.conf import settings
from .serializers import (
    TaskStatusOpenSerializer,
    TaskStatusUpdateNeededSerializer,
    TaskStatusScheduledSerializer,
    TaskStatusClosedSerializer,
    TaskStatusInProgressSerializer,
)
from .constants import DATA_DIR, TASKS_FILE


class TaskStatusViewSet(viewsets.ViewSet):
    @staticmethod
    def get_task_data(task_id: int = None):
        csv_path = os.path.join(settings.BASE_DIR, DATA_DIR, TASKS_FILE)
        try:
            with open(csv_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                if task_id:
                    return next(
                        (row for row in reader if row["id"] == str(task_id)), None
                    )
                return list(reader)
        except FileNotFoundError:
            return None

    @staticmethod
    def get_serializer_class(status: str):
        return {
            "open": TaskStatusOpenSerializer,
            "update-needed": TaskStatusUpdateNeededSerializer,
            "scheduled": TaskStatusScheduledSerializer,
            "closed": TaskStatusClosedSerializer,
            "in-progress": TaskStatusInProgressSerializer,
        }.get(status)

    def retrieve(self, request, pk: int = None):
        task = self.get_task_data(pk)
        if task is None:
            return Response({"error": "Task not found"}, status=404)
        serializer_class = self.get_serializer_class(task["status"])
        if serializer_class is None:
            return Response({"error": "Invalid task status"}, status=400)
        serializer = serializer_class(task)
        return Response(serializer.data)

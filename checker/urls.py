from rest_framework.routers import DefaultRouter
from .views import TaskStatusViewSet

router = DefaultRouter()
router.register(r"task", TaskStatusViewSet, basename="task")

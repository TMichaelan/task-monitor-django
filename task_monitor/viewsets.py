from rest_framework.viewsets import GenericViewSet


class RetrieveOnlyViewSet(GenericViewSet):
    throttle_scope = "task_status"

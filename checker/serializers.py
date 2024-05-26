# pylint: disable=no-self-use

import datetime
from typing import Any, Optional
from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.CharField()
    outcome = serializers.SerializerMethodField()
    fake_outcome_reason = serializers.SerializerMethodField()
    photos_to_resubmit = serializers.SerializerMethodField()
    answer_time = serializers.IntegerField()
    date_created = serializers.SerializerMethodField()
    due_date = serializers.SerializerMethodField()
    date_closed = serializers.SerializerMethodField()

    def get_outcome(self, obj: Any) -> Optional[str]:
        return obj.get("outcome") or None

    def get_fake_outcome_reason(self, obj: Any) -> Optional[str]:
        outcome = obj.get("outcome")
        if outcome in ["fake", "UTV"]:
            return obj.get("fake_outcome_reason") or None
        return None

    def get_photos_to_resubmit(self, obj: Any) -> Optional[str]:
        return obj.get("photos_to_resubmit") or None

    def get_date_created(self, obj: Any) -> Optional[str]:
        return self.convert_timestamp(obj.get("date_created"))

    def get_due_date(self, obj: Any) -> Optional[str]:
        return self.convert_timestamp(obj.get("due_date"))

    def get_date_closed(self, obj: Any) -> Optional[str]:
        return self.convert_timestamp(obj.get("date_closed"))

    @staticmethod
    def convert_timestamp(timestamp: Any) -> Optional[str]:
        if timestamp:
            return datetime.datetime.fromtimestamp(int(timestamp)).isoformat()
        return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        fields = self.Meta.base_fields + self.Meta.extra_fields
        response_data = {
            field: representation[field] for field in fields if field in representation
        }
        if "outcome" in response_data and response_data["outcome"] not in [
            "fake",
            "UTV",
        ]:
            response_data.pop("fake_outcome_reason", None)
        return response_data

    class Meta:
        base_fields = [
            "id",
            "status",
            "answer_time",
            "date_created",
            "due_date",
        ]
        extra_fields = []

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class TaskStatusOpenSerializer(TaskSerializer):
    class Meta(TaskSerializer.Meta):
        extra_fields = []


class TaskStatusUpdateNeededSerializer(TaskSerializer):
    class Meta(TaskSerializer.Meta):
        extra_fields = [
            "photos_to_resubmit",
        ]


class TaskStatusScheduledSerializer(TaskSerializer):
    class Meta(TaskSerializer.Meta):
        extra_fields = [
            "outcome",
            "fake_outcome_reason",
        ]


class TaskStatusClosedSerializer(TaskSerializer):
    class Meta(TaskSerializer.Meta):
        extra_fields = [
            "outcome",
            "date_closed",
            "fake_outcome_reason",
        ]


class TaskStatusInProgressSerializer(TaskSerializer):
    class Meta(TaskSerializer.Meta):
        extra_fields = []

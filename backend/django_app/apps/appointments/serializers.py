from rest_framework import serializers
from django.utils.timezone import now
from .models import Appointment
from apps.services.models import Service


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = (
            "id",
            "vehicle",
            "service",
            "staff",
            "start_time",
            "end_time",
            "status",
        )
        read_only_fields = ("status", "end_time")

    def validate(self, data):
        start_time = data.get("start_time")
        service = data.get("service")

        if start_time < now():
            raise serializers.ValidationError(
                "Termin ne može biti u prošlosti."
            )

        duration = service.duration_minutes
        data["end_time"] = start_time + service.duration_minutes * service.duration_minutes.__class__(60)

        return data
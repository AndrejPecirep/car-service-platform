from datetime import timedelta

from django.utils.timezone import now
from rest_framework import serializers

from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    vehicle_display = serializers.CharField(source="vehicle.__str__", read_only=True)
    service_name = serializers.CharField(source="service.name", read_only=True)
    staff_name = serializers.SerializerMethodField()

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
            "vehicle_display",
            "service_name",
            "staff_name",
        )
        read_only_fields = ("status", "end_time")

    def get_staff_name(self, obj):
        if not obj.staff:
            return None
        return f"{obj.staff.first_name} {obj.staff.last_name}".strip() or obj.staff.email

    def validate(self, data):
        start_time = data.get("start_time")
        service = data.get("service")
        if start_time and start_time < now():
            raise serializers.ValidationError("The appointment cannot be scheduled in the past.")
        if start_time and service:
            data["end_time"] = start_time + timedelta(minutes=service.duration_minutes)
        return data

from datetime import timedelta

from django.utils.timezone import now
from rest_framework import serializers

from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    vehicle_label = serializers.SerializerMethodField(read_only=True)
    service_label = serializers.CharField(source="service.name", read_only=True)
    staff_label = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Appointment
        fields = (
            "id",
            "vehicle",
            "vehicle_label",
            "service",
            "service_label",
            "staff",
            "staff_label",
            "start_time",
            "end_time",
            "status",
        )
        read_only_fields = ("status", "end_time")

    def validate(self, data):
        start_time = data.get("start_time")
        service = data.get("service")

        if start_time and start_time < now():
            raise serializers.ValidationError("Termin ne može biti u prošlosti.")

        if service and start_time:
            data["end_time"] = start_time + timedelta(minutes=service.duration_minutes)

        return data

    def get_vehicle_label(self, obj):
        return str(obj.vehicle)

    def get_staff_label(self, obj):
        return str(obj.staff) if obj.staff else None

from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Appointment
from .serializers import AppointmentSerializer
from .services import is_time_slot_available


class AppointmentViewSet(ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Appointment.objects.select_related("vehicle", "service", "staff", "vehicle__owner").order_by("-start_time")
        if user.role == "ADMIN":
            return queryset
        if user.role == "STAFF":
            return queryset.filter(staff=user)
        return queryset.filter(vehicle__owner=user)

    def perform_create(self, serializer):
        staff = serializer.validated_data.get("staff")
        start_time = serializer.validated_data.get("start_time")
        end_time = serializer.validated_data.get("end_time")

        if staff and not is_time_slot_available(staff, start_time, end_time):
            raise ValidationError("The selected staff member is not available for this time slot.")

        serializer.save(status=Appointment.Status.CONFIRMED)

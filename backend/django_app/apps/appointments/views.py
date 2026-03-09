from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from .models import Appointment
from .serializers import AppointmentSerializer
from .services import is_time_slot_available


class AppointmentViewSet(ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "ADMIN":
            return Appointment.objects.all()

        if user.role == "STAFF":
            return Appointment.objects.filter(staff=user)

        return Appointment.objects.filter(vehicle__owner=user)

    def perform_create(self, serializer):
        staff = serializer.validated_data.get("staff")
        start_time = serializer.validated_data.get("start_time")
        end_time = serializer.validated_data.get("end_time")

        if staff and not is_time_slot_available(staff, start_time, end_time):
            raise ValidationError(
                "Odabrani termin nije dostupan za ovog djelatnika."
            )

        serializer.save(status="CONFIRMED")
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Vehicle
from .serializers import VehicleSerializer


class VehicleViewSet(ReadOnlyModelViewSet):
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Vehicle.objects.select_related("owner").order_by("-created_at")
        if user.role == "ADMIN":
            return queryset
        if user.role == "STAFF":
            return queryset
        return queryset.filter(owner=user)

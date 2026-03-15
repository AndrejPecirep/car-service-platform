from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Service
from .serializers import ServiceSerializer


class ServiceViewSet(ReadOnlyModelViewSet):
    queryset = Service.objects.filter(is_active=True).order_by("name")
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

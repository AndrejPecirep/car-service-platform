from django.contrib.auth.hashers import check_password, make_password
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.appointments.models import Appointment
from apps.services.models import Service
from apps.vehicles.models import Vehicle
from .models import User
from .serializers import UserSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by("-created_at")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class StaffViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.filter(role=User.Role.STAFF).order_by("first_name", "last_name")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class CustomerViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.filter(role=User.Role.CLIENT).order_by("first_name", "last_name")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {
                "vehicle_count": Vehicle.objects.count(),
                "customer_count": User.objects.filter(role=User.Role.CLIENT).count(),
                "appointment_count": Appointment.objects.filter(status__in=[Appointment.Status.PENDING, Appointment.Status.CONFIRMED]).count(),
                "service_count": Service.objects.filter(is_active=True).count(),
            }
        )


class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        if not check_password(password, user.password):
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": UserSerializer(user).data,
        })


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        password = request.data.get("password")
        if not email or not first_name or not last_name or not password:
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({"error": "A user with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=make_password(password),
            role=User.Role.CLIENT,
        )
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": UserSerializer(user).data,
        }, status=status.HTTP_201_CREATED)

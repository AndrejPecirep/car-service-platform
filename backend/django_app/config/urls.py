from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.appointments.views import AppointmentViewSet
from apps.services.views import ServiceViewSet
from apps.users import views as user_views
from apps.users.views import UserViewSet
from apps.vehicles.views import VehicleViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"vehicles", VehicleViewSet, basename="vehicle")
router.register(r"services", ServiceViewSet, basename="service")
router.register(r"appointments", AppointmentViewSet, basename="appointment")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/auth/login/", user_views.LoginView.as_view(), name="login"),
    path("api/auth/register/", user_views.RegisterView.as_view(), name="register"),
]

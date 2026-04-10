from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.appointments.views import AppointmentViewSet
from apps.services.views import ServiceViewSet
from apps.users import views as user_views
from apps.users.views import CustomerViewSet, StaffViewSet, UserViewSet
from apps.vehicles.views import VehicleViewSet
from config.health import health

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"staff", StaffViewSet, basename="staff")
router.register(r"customers", CustomerViewSet, basename="customer")
router.register(r"vehicles", VehicleViewSet, basename="vehicle")
router.register(r"services", ServiceViewSet, basename="service")
router.register(r"appointments", AppointmentViewSet, basename="appointment")

urlpatterns = [
    path("health/", health, name="health"),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/auth/login/", user_views.LoginView.as_view(), name="login"),
    path("api/auth/register/", user_views.RegisterView.as_view(), name="register"),
    path("api/dashboard/summary/", user_views.DashboardSummaryView.as_view(), name="dashboard-summary"),
]

from django.test import TestCase
from django.utils.timezone import now, timedelta
from apps.users.models import User
from apps.vehicles.models import Vehicle
from apps.services.models import Service
from .models import Appointment


class AppointmentTest(TestCase):

    def setUp(self):
        self.staff = User.objects.create_user(
            email="staff@example.com",
            password="pass",
            role="STAFF",
            first_name="Staff",
            last_name="User"
        )

        self.client = User.objects.create_user(
            email="client@example.com",
            password="pass",
            first_name="Client",
            last_name="User"
        )

        self.vehicle = Vehicle.objects.create(
            owner=self.client,
            brand="Audi",
            model="A4",
            year=2021,
            license_plate="ZG-9999-AA"
        )

        self.service = Service.objects.create(
            name="Major Service",
            duration_minutes=120,
            price=300
        )

    def test_create_appointment(self):
        start = now() + timedelta(days=1)
        end = start + timedelta(minutes=120)

        appointment = Appointment.objects.create(
            vehicle=self.vehicle,
            service=self.service,
            staff=self.staff,
            start_time=start,
            end_time=end
        )

        self.assertEqual(appointment.status, "PENDING")
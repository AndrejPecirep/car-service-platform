from django.test import TestCase
from apps.users.models import User
from .models import Vehicle


class VehicleModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="client@example.com",
            password="password123",
            first_name="Client",
            last_name="User"
        )

    def test_create_vehicle(self):
        vehicle = Vehicle.objects.create(
            owner=self.user,
            brand="Volkswagen",
            model="Golf",
            year=2020,
            license_plate="ZG-1234-AA"
        )

        self.assertEqual(vehicle.owner.email, "client@example.com")
        self.assertEqual(vehicle.brand, "Volkswagen")
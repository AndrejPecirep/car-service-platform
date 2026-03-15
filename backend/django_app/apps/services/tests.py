from django.test import TestCase
from .models import Service


class ServiceModelTest(TestCase):

    def test_create_service(self):
        service = Service.objects.create(
            name="Basic Service",
            duration_minutes=60,
            price=120.00
        )

        self.assertEqual(service.name, "Basic Service")
        self.assertEqual(service.duration_minutes, 60)
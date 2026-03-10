from django.db import models
from django.conf import settings


class Vehicle(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="vehicles"
    )
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    license_plate = models.CharField(max_length=20, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.license_plate})"
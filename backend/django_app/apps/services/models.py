from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField(help_text="Service duration in minutes")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.duration_minutes} min)"

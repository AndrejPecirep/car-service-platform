from django.contrib import admin
from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "license_plate", "owner")
    search_fields = ("brand", "model", "license_plate")
    list_filter = ("brand",)
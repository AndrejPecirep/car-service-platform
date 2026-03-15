from rest_framework import serializers

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField()

    class Meta:
        model = Vehicle
        fields = ("id", "owner", "owner_name", "brand", "model", "year", "license_plate", "created_at")

    def get_owner_name(self, obj):
        return f"{obj.owner.first_name} {obj.owner.last_name}".strip() or obj.owner.email

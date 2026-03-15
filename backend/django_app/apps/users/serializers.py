from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "role",
            "created_at",
        )

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password")

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

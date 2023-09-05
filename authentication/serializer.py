from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import IntegrityError


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    device_type = serializers.CharField(max_length=50, required=False, allow_blank=True)
    fcm_token = serializers.CharField(max_length=500, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ("id", "email", "password", "device_type", "fcm_token")

    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                username=validated_data["email"],
                email=validated_data["email"],
                password=validated_data["password"],
                is_active=False,
            )
        except IntegrityError:
            raise serializers.ValidationError(
                {
                    "status": False,
                    "message": "Email is already registered",
                    "data": None,
                }
            )
        return user

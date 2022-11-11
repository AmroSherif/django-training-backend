from rest_framework import serializers
from .models import ExtendedUser
from django.contrib.auth.password_validation import (
    validate_password as validate_pass,
    MinimumLengthValidator,
    CommonPasswordValidator,
)
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = ["id", "username", "email", "bio"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=200, write_only=True)

    def validate_password(self, value):
        validate_pass(
            password=value,
            password_validators=[
                MinimumLengthValidator(min_length=8),
                CommonPasswordValidator(),
            ],
        )
        if (
            "confirm_password" not in self.initial_data
            or value != self.initial_data["confirm_password"]
        ):
            raise serializers.ValidationError("Password confirmation mismatched")
        return value

    class Meta:
        model = ExtendedUser
        fields = "__all__"

    def create(self, validated_data):
        return ExtendedUser.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
        )


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user:
            return user
        raise serializers.ValidationError("Username or password is incorrect")

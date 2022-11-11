from rest_framework import serializers
from .models import Artist
from users.models import ExtendedUser


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "username", "stage_name", "email", "bio"]

    def create(self, validated_data):
        return Artist.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            stage_name=validated_data["stage_name"],
        )

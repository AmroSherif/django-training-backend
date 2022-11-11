from rest_framework import serializers
from .models import Album, Song
from artists.serializers import ArtistSerializer


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "name", "image", "audio"]


class AlbumSerializer(serializers.ModelSerializer):
    # songs = SongSerializer(many=True)

    class Meta:
        model = Album
        fields = "__all__"


class ApprovedAlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Album
        fields = "__all__"

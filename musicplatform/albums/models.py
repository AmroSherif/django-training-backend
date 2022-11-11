from django.db import models
from artists.models import Artist
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from musicplatform.settings import STATIC_URL


class Album(models.Model):
    name = models.CharField(max_length=30, default="New Album")
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, null=True, related_name="albums"
    )
    is_approved = models.BooleanField(
        default=False, help_text=" Approve the album if its name is not explicit"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "albums"


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    name = models.CharField(max_length=30, default=album.name)
    image = models.ImageField(upload_to=STATIC_URL)
    thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(50, 50)],
        format="JPEG",
        options={"quality": 100},
    )
    audio = models.FileField(upload_to=STATIC_URL)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "songs"

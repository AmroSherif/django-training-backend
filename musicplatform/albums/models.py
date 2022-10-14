from django.db import models
from artists.models import Artist


class Album(models.Model):
    name = models.CharField(max_length=30, default="New Album")
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, null=True, related_name="albums"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "albums"

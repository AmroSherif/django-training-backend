from django.db import models


class Artist(models.Model):
    stage_name = models.CharField(max_length=30, unique=True)
    social_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.stage_name

    class Meta:
        db_table = "artists"
        ordering = ["stage_name"]

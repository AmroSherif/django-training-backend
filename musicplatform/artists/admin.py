from django.contrib import admin
from .models import Artist
from albums.models import Album


class AlbumTabular(admin.TabularInline):
    model = Album
    readonly_fields = ["creation_datetime"]


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["stage_name", "social_link", "get_albums_count"]
    inlines = [AlbumTabular]

    def get_albums_count(self, obj):
        return obj.albums.filter(is_approved=True).count()

    get_albums_count.short_description = "Approved albums"

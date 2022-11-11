from django.contrib import admin
from .models import Album, Song
from .forms import SongValidation


class SongTabular(admin.TabularInline):
    model = Song
    formset = SongValidation


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["name", "cost", "artist"]
    readonly_fields = ["creation_datetime"]
    inlines = [SongTabular]

from django.urls import path
from .views import ArtistView

urlpatterns = [path("", ArtistView.as_view())]

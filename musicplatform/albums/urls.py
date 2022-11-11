from django.urls import path
from .views import AlbumView, ApprovedAlbumView, SingleAlbumView

urlpatterns = [
    path("", AlbumView.as_view()),
    path("<int:id>/", SingleAlbumView.as_view()),
    path("approved/", ApprovedAlbumView.as_view()),
]

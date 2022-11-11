from .models import Artist
from rest_framework.response import Response
from rest_framework import status


class ArtistAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return Response(
                "You are not authenticated", status=status.HTTP_403_FORBIDDEN
            )

        if Artist.objects.filter(pk=request.user.id).exists():
            response = self.get_response(self, request)
            return response
        return Response("You are not an artist", status=status.HTTP_403_FORBIDDEN)

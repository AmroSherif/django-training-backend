from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist
from .serializers import ArtistSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status

# from .middlewares import SimpleMiddleware


class ArtistView(APIView):
    def get(self, request):
        return Response(
            ArtistSerializer(Artist.objects.all(), many=True).data,
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        artist_serializer = ArtistSerializer(data=request.data)
        if artist_serializer.is_valid():
            artist_serializer.save()
            return Response(artist_serializer.data, status=status.HTTP_201_CREATED)
        return Response(artist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

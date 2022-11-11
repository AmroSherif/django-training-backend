from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlbumSerializer, ApprovedAlbumSerializer
from .models import Album
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.pagination import LimitOffsetPagination
from artists.middlewares import ArtistAuthenticationMiddleware
from artists.models import Artist
from .filters import AlbumFilter


class AlbumView(APIView, LimitOffsetPagination):
    def get(self, request):
        query = AlbumFilter(request.GET, queryset=Album.objects.all())
        result = self.paginate_queryset(query.qs, request, view=self)
        return Response(
            AlbumSerializer(result, many=True).data,
            status=status.HTTP_200_OK,
        )

    @ArtistAuthenticationMiddleware
    def post(self, request):
        album_serializer = AlbumSerializer(data=request.data)
        if album_serializer.is_valid():
            album_serializer.save(artist=Artist.objects.get(pk=request.user.id))
            return Response(album_serializer.data)
        return Response(album_serializer.errors)


class ApprovedAlbumView(APIView, LimitOffsetPagination):
    def get(self, request):
        result = self.paginate_queryset(
            Album.objects.filter(is_approved=True), request, view=self
        )
        return Response(
            ApprovedAlbumSerializer(result, many=True).data,
            status=status.HTTP_200_OK,
        )


class SingleAlbumView(APIView):
    def get(self, request, id):
        try:
            album_serializer = AlbumSerializer(Album.objects.get(pk=id))
            return Response(
                album_serializer.data,
                status=status.HTTP_200_OK,
            )
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            album_serializer = AlbumSerializer(
                data=request.data, instance=Album.objects.get(pk=id)
            )
            if album_serializer.is_valid():
                album_serializer.save()
                return Response(album_serializer.data)
            return Response(album_serializer.errors)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

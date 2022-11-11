from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import ExtendedUser
from django.core.exceptions import ObjectDoesNotExist
from .middlewares import UserEditMiddleware


class SingleUserView(APIView):
    def get(self, request, id):
        try:
            user = UserSerializer(ExtendedUser.objects.get(pk=id))
            return Response(user.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @UserEditMiddleware
    def put(self, request, id):
        try:
            updated_user = UserSerializer(
                data=request.data, instance=ExtendedUser.objects.get(pk=id)
            )
            if updated_user.is_valid():
                updated_user.save()
                return Response(updated_user.data)
            return Response(updated_user.errors)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @UserEditMiddleware
    def patch(self, request, id):
        try:
            updated_user = UserSerializer(
                data=request.data,
                instance=ExtendedUser.objects.get(pk=id),
                partial=True,
            )
            if updated_user.is_valid():
                updated_user.save()
                return Response(updated_user.data)
            return Response(updated_user.errors)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

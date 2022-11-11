from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserRegistrationSerializer, UserLoginSerializer
from knox.models import AuthToken
from rest_framework.permissions import AllowAny


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        extended_user_serializer = UserRegistrationSerializer(data=request.data)
        if extended_user_serializer.is_valid():
            extended_user_serializer.save()
            return Response(
                extended_user_serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            extended_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        login_user_serializer = UserLoginSerializer(data=request.data)
        if login_user_serializer.is_valid():
            user = login_user_serializer._validated_data
            return Response(
                {
                    "token": AuthToken.objects.create(user)[1],
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "bio": user.bio,
                    },
                }
            )
        return Response(login_user_serializer.errors)

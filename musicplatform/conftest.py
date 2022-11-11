import pytest
from users.models import ExtendedUser
from rest_framework.test import APIClient
from knox.models import AuthToken


@pytest.fixture
def auth_client():
    def auth(user: ExtendedUser = None):
        client = APIClient()
        if user:
            client.credentials(
                HTTP_AUTHORIZATION="Token " + AuthToken.objects.create(user)[1]
            )
        return client

    return auth


@pytest.fixture
def send_user(db, auth_client):
    return auth_client(
        ExtendedUser.objects.create_user(
            username="karem",
            password="qweewq123",
            email="karem@yahoo.com",
        )
    )


@pytest.fixture
def send_no_user(auth_client):
    return auth_client()

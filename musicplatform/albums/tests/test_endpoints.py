import pytest
from rest_framework import status


def test_authenticated(send_user):
    client = send_user
    response = client.get("/albums/")
    assert response.status_code == status.HTTP_200_OK


# will not work since we changed the global permission to allow any
# def test_not_authenticated(send_no_user):
#     client = send_no_user
#     response = client.get("/albums/")
#     assert response.status_code == status.HTTP_401_UNAUTHORIZED

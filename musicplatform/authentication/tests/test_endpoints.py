import pytest
from rest_framework import status
from rest_framework.test import APIClient


def test_registration_missing_info(db):
    client = APIClient()
    response = client.post(
        "/authentication/register/",
        {"username": "akram", "password": "qweewq123"},
        format="json",
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_registration_complete_info(db):
    client = APIClient()
    response = client.post(
        "/authentication/register/",
        {
            "username": "akram",
            "password": "qweewq123",
            "confirm_password": "qweewq123",
            "email": "akram@yahoo.com",
        },
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED

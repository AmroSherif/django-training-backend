from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.validators import UniqueValidator


class ExtendedUser(AbstractUser):
    bio = models.CharField(max_length=256, blank=True)
    email = models.EmailField(max_length=256, blank=False, null=False, unique=True)

    class Meta:
        db_table = "users"

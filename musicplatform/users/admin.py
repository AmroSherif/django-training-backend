from django.contrib import admin
from .models import ExtendedUser
from .forms import ExtendedUserForm
from django.contrib.auth.admin import UserAdmin


@admin.register(ExtendedUser)
class ExtendedUserAdmin(admin.ModelAdmin):
    form = ExtendedUserForm

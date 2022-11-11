from django.urls import path
from .views import RegistrationView, LoginView
from knox.views import LogoutView

urlpatterns = [
    path("register/", RegistrationView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
]

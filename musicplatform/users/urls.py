from django.urls import path
from .views import SingleUserView

urlpatterns = [path("<int:id>", SingleUserView.as_view())]

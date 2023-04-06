from django.urls import path

from . import views
from .views import CheckView

urlpatterns = [
    path("", views.index, name = 'index'),
    path("<str:room_name>/", views.room, name="room"),
    path("checkview", CheckView.as_view(), name="checkview"),
]
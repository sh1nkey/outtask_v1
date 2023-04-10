from django.urls import path

from . import views
from .views import ChatListView, message_save

urlpatterns = [
    path("chat", views.index, name = 'chat'),
    path("<str:room_name>/", views.room, name="room"),
    path("chatlistview", ChatListView.as_view(), name="chatlistview"),
    path('<uuid:room_id>/messages/save/', message_save, name='save_message'),
]
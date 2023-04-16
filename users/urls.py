from django.urls import path

from users.views import LoginUpdate, VUZUpdate, Profile, DeleteOffers

urlpatterns= [
    path("profile/", Profile.as_view(), name="profile"),
    path("login-update/<int:pk>/",  LoginUpdate.as_view(), name="login-update"),
    path("vuz-update/<int:pk>/",  VUZUpdate.as_view(), name="vuz-update"),
    path("offer-delete/<int:pk>/",  DeleteOffers.as_view(), name="deleteorder"),
]
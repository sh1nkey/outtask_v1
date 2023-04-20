from django.urls import path

from users.views import LoginUpdate, VUZUpdate, Profile, DeleteOffers, DeleteOrders, PerCabView, LinkUpdate

urlpatterns= [
    path("profile/", Profile.as_view(), name="profile"),
    path("login-update/<int:pk>/",  LoginUpdate.as_view(), name="login-update"),
    path("vuz-update/<int:pk>/",  VUZUpdate.as_view(), name="vuz-update"),
    path("link-update/<int:pk>/",  LinkUpdate.as_view(), name="link-update"),
    path("offer-delete/<int:pk>/",  DeleteOffers.as_view(), name="deleteoffer"),
    path("order-delete/<int:pk>/",  DeleteOrders.as_view(), name="deleteorder"),
    path("personal_cabinet/",  PerCabView.as_view(), name="personal_cabinet"),
]
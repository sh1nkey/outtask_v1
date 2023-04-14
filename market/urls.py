from django.urls import path
from market.views import OfferCreationView, MarketListView, ProfileView

urlpatterns = [
    path("", MarketListView.as_view(), name="markett"),
    path("create-offer/", OfferCreationView.as_view(), name = 'createoffer'),
    path("profile/",  ProfileView.as_view(), name="profile"),

]
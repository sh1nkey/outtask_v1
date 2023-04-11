from django.urls import path
from market.views import OfferCreationView, MarketListView, ProfileView

urlpatterns = [
    path("create-offer/", OfferCreationView.as_view(), name = 'createoffer'),
    path("", MarketListView.as_view(), name="marketlistview"),
    path("profile/", ProfileView.as_view(), name="profile"),

]
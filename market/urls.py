from django.urls import path
from market.views import OfferCreationView, MarketListView, OfferDelete

urlpatterns = [
    path("", MarketListView.as_view(), name="markett"),
    path("create-offer/", OfferCreationView.as_view(), name = 'createoffer'),
]
from django.urls import path
from market.views import OfferCreationView, MarketListView, OrderAdd
from outtask import settings
urlpatterns = [
    path("", MarketListView.as_view(), name='markett'),
    path("create-offer/", OfferCreationView.as_view(), name = 'createoffer'),
    path("add-order/<int:pk>/", OrderAdd.as_view(), name = 'addoffer'),
]
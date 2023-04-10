from django.urls import path


from market.views import OfferCreationView, MarketListView

urlpatterns = [
    path("create-offer/", OfferCreationView.as_view(), name = 'createoffer'),
    path("", MarketListView.as_view(), name="marketlistview"),
]
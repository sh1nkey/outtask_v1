from django.urls import path


from market.views import  OfferCreationView

urlpatterns = [
    path("create-offer/", OfferCreationView.as_view(), name = 'createoffer'),
]
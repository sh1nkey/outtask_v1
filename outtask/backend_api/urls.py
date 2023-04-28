from django.urls import path
from backend_api.views import MarketRestView

urlpatterns = [
    path('market/', MarketRestView.as_view(), name='rest_market')
]
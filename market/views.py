from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from market.models import Offer


class MarketListView(ListView):
    model = Offer
    template_name = 'market/market.html'
    title = 'test'

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

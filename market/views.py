from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView

from market.models import Offer
from users.models import Uni


class MarketListView(ListView):
    template_name = 'market/market.html'
    title = 'test'

    def get_queryset(self):
        offers = Offer.objects.all()
        unis = Uni.objects.all()
        unis_check = self.kwargs.get('uni_name')
        return offers.filter(uni_name=unis_check) if unis_check else offers, unis #допилить фильрацию по ВУЗу

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers'] = Offer.objects.all()
        context['unis'] = Uni.objects.all()
        return context

class IndexView(TemplateView):
    template_name = 'market/index.html' #

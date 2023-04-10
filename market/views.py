from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView

from market.forms import UniForm
from market.models import Offer
from users.models import Uni


class MarketListView(ListView):
    template_name = 'market/market.html'
    title = 'Маркет'

    def get_queryset(self):
        offers = Offer.objects.all()
        unis_check = self.request.GET.get('uni_name')
        return offers.filter(user__uni__pk=unis_check) if unis_check else offers

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = UniForm()
        context['offers'] = self.get_queryset()
        context['unis'] = Uni.objects.all()
        context['form'] = form
        return context


class IndexView(TemplateView):
    template_name = 'market/index.html' #
